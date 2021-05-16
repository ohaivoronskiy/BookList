<template>
  <div class="header">
    <div v-if="accessToken!=null" class="logout">
      <p @click="logout()" ><i class="el-icon-switch-button"></i>Logout</p>
    </div>
    <h2 class="logo">BOOK LIST</h2>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'NavBar',
  computed: mapState(['accessToken']),
  methods: {
    logout(){
      this.$store.dispatch('userLogout')
        .then(() => {
          this.$router.push({ name: 'login' })
        })
    }
  }
}
</script>

<style lang="scss">
.header {
  padding: 20px 20px;
  color: #f0f4f8;
  display: flex;
  flex-direction: column;
  align-items: center;
  h1,
  h2,
  h3 {
    color: #f0f4f8;
    padding: 0;
    margin: 0;
  }
}
.header {
  padding: 10px 20px;
  .logo {
    letter-spacing: 3px;
    padding-top: 15px;
    padding-bottom: 15px;
  }
  .logout{
    position: absolute;
    right: 0;
    margin-right: 20px;
    top: 0px;
  }
}
</style>