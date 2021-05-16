from django.db import transaction
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


from .models import Book
from .serializers import BookSerializer


class BookViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        user = self.request.user
        books = Book.objects.filter(owner=user.id)
        return books

    def perform_create(self, serializer):
        kwargs = {
            'owner': self.request.user
        }
        serializer.save(**kwargs)

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        with transaction.atomic():
            try:
                instance = self.get_object()
                instance.id = kwargs.get('pk')
                serializer = BookSerializer(instance=instance, data=request.data)

                if serializer.is_valid(raise_exception=True):
                    self.perform_update(serializer)
                    return Response({"status": True, "results": "Datos actualizados correctamente"},
                                    status=status.HTTP_201_CREATED)
            except ValidationError as err:
                return Response({"status": False, "error_description": err.detail}, status=status.HTTP_400_BAD_REQUEST)