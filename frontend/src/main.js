import Vue from 'vue'
import App from './App.vue'
import './plugins/element.js'
import store from './store'
import router from './routes.js'
import titleMixin from './titleMixin'



Vue.mixin(titleMixin)

Vue.config.productionTip = false

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresLogin)) {
    if (!store.getters.loggedIn) {
      next({ name: 'login' })
    } else {
      next()
    }
  } else {
    next()
  }
})

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
