import Vue from 'vue'
import VueRouter from 'vue-router'
import BookList from './components/BookList'
import Login from './components/Login'

Vue.use(VueRouter)

export default new VueRouter({
    mode: 'history',
    routes: [
        {
        path: '/books',
        name: 'books',
        component: BookList,
        meta: {
            requiresLogin: true
          }
        },
        {
        path: '/login',
        name: 'login',
        component: Login,
        }
    ]
})