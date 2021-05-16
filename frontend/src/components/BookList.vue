<template>
  <section>
    <NavBar/>
    <el-row>
      <el-button type="success" @click="dialogFormVisible = true" class="pull-right" >Add new book</el-button>
    </el-row>
    <el-row>
      <el-dialog title="Add your new book" :visible.sync="dialogFormVisible">
        <el-form :model="bookForm" :rules="rules" ref="form" @submit.native.prevent="submitForm">
          <el-form-item label="Author" prop="author">
            <el-input v-model="bookForm.author" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="Title" prop="title" >
            <el-input v-model="bookForm.title" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="Description" prop="description">
            <el-input v-model="bookForm.description" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label = "Book poster" prop="poster">
            <el-input type="file" v-model="bookForm.poster"></el-input>
          </el-form-item>
            <el-button @click="dialogFormVisible = false" class="dialog-footer">Cancel</el-button>
            <el-button
                type="primary"
                :loading="loading"
                native-type="submit"
                class="dialog-footer"
                block
            >Confirm</el-button>
        </el-form>
      </el-dialog>
      <div class="book-table">
        <el-table
          ref="filterTable"
          :data="tableData"
          >
          <el-table-column
            prop="author"
            label="Author"
            sortable
            column-key="author"
          >
          </el-table-column>
          <el-table-column
            prop="title"
            label="Title"
            sortable
          >
          </el-table-column>
          <el-table-column
            prop="description"
            label="Description"
            sortable
          >
          </el-table-column>
          <el-table-column
            prop="actions"
            label="Actions"
          >
            <template  slot-scope="scope">
              <el-button type="primary" icon="el-icon-edit" circle @click="editBook(scope.row)"></el-button>
              <el-button type="danger" icon="el-icon-delete" circle @click="deleteBook(scope.row.id)"></el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
    </el-row>
  </section>
</template>

<script>
  import NavBar from "@/components/NavBar";
    import {apiConfig} from "@/api-config";
    import { mapState } from "vuex"


    export default {
      name: 'books',
      components: {NavBar},
      computed: mapState(['accessToken']),
      title: 'Your books - Book List',
      data() {
        return {
          tableData:[],
          dialogFormVisible: false,
          loading: false,
          bookForm: {
            id: '',
            author: '',
            title: '',
            description: '',
            poster: ''
          },
          rules: {
            author: [
              {
                required: true,
                message: 'Author is required',
                trigger: 'blur'
              },
              {
                min: 2,
                max: 139,
                message: 'Author length should be at least 3 and no more than 140 characters',
                trigger: 'blur'
              }
            ],
            title: [
              {
                required: true,
                message: 'Title is required',
                trigger: 'blur'
              },
              {
                min: 4,
                max: 140,
                message: 'Title length should be at least 5 and no more than 140 characters',
                trigger: 'blur'
              }
            ],
            description: [
              {
                required: true,
                message: 'Description is required',
                trigger: 'blur'
              },
              {
                min: 4,
                max: 255,
                message: 'Description length should be at least 5 and no more than 256 characters',
                trigger: 'blur'
              }
            ],
          }
        }
      },
      async mounted() {
        await this.getData()
    },
    methods: {
      getBearer() {
        return `Bearer ${this.$store.state.accessToken}`
      },
      formData(bookData){
        let data = new FormData()
        data.append('title', bookData.title)
        data.append('author', bookData.author)
        data.append('description', bookData.description)
        data.append('id', bookData.id)
        data.append('poster', bookData.poster)

        return data
      },
      resetForm() {
        this.bookForm = {
          id: '',
          author: '',
          title: '',
          description: '',
          poster: '',
        }
      },
      async getData(){
         await apiConfig
        .get('/api/books/', { headers: { Authorization: this.getBearer()}})
        .then(response => {
          this.tableData = response.data
        })
        .catch(function (error) {
          console.log(error);
        })
      },
      async deleteBook(id){
        await apiConfig.delete(`/api/books/${id}`, { headers: {
          Authorization: this.getBearer()}})
          .then(async () => {
            await this.getData()
            this.$message.error("Book deleted");
          })
          .catch(function (error) {
            console.log(error);
          })
      },
      async submitForm(){
        const data = this.getData(this.bookForm)
        if (!data.id) {
          await apiConfig.post('/api/books/', data, { headers: {
            Authorization: this.getBearer(), 'Content-Type': 'multipart/form-data'}})
           .then(async () => {
              this.dialogFormVisible = false
              this.resetForm();
              await this.getData()
              this.$message.success("Book added successful");
            })
           .catch(function (error) {
              console.log(error);
           })
        }
        else {
          await apiConfig.fetch(`/api/books/${this.bookForm.id}/`, this.bookForm, { headers: {
            Authorization: this.getBearer(), 'Content-Type': 'multipart/form-data'}})
             .then( async () => {
                this.dialogFormVisible = false
                this.resetForm();
                await this.getData()
                this.$message.success("Book edited successful");
              })
             .catch(function (error) {
                console.log(error);
             })
        }
      },
      editBook(data) {
        this.bookForm = {
          author: data.author,
          title: data.title,
          description: data.description,
          owner: data.owner,
          id: data.id,
          poster: data.poster,
        }
        this.dialogFormVisible = true
      }
    }
  }
</script>

<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.pull-right{
    position: relative;
    margin-right: 20px;
    float: right;
    margin-top: 20px;
    margin-bottom: 20px;
}
.book-table{
  margin-left: 20px;
  margin-right: 20px;
}
</style>