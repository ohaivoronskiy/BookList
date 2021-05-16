<template>
  <div>
    <NavBar/>
    <div class="login">
      <el-card>
        <h2>Login</h2>
        <el-form
          class="login-form"
          :model="model"
          :rules="rules"
          ref="form"
          @submit.native.prevent="login"
        >
          <el-form-item prop="username">
            <el-input v-model="model.username" placeholder="Username"></el-input>
          </el-form-item>
          <el-form-item prop="password">
            <el-input
              v-model="model.password"
              placeholder="Password"
              type="password"
            >
            </el-input>
          </el-form-item>
          <el-form-item>
            <el-button
              :loading="loading"
              class="login-button"
              type="primary"
              native-type="submit"
              block
            >Login</el-button>
          </el-form-item>
        </el-form>
      </el-card>
    </div>
  </div>
</template>

<script>
import NavBar from "@/components/NavBar";

export default {
  name: 'login',
  title: 'Login - Book List',
  components: {NavBar},
  data() {
    return {
      username: '',
      password: '',
      loading: false,
      model: {
        username: '',
        password: ''
      },
      rules: {
        username: [
          {
            required: true,
            message: 'Username is required',
            trigger: 'blur'
          },
          {
            min: 4,
            message: 'Username length should be at least 5 characters',
            trigger:'blur'
          }
        ],
        password: [
          { required: true, message: 'Password is required', trigger: 'blur' },
          {
            min: 5,
            message: 'Password length should be at least 5 characters',
            trigger: 'blur'
          }
        ]
      }
    };
  },
  methods: {
    login () {
      this.$store.dispatch('userLogin', {
        username: this.model.username,
        password: this.model.password
      })
      .then(() => {
        this.$router.push({ name: 'books' })
        this.$message.success('Login successful');
      })
      .catch(error => {
        console.log(error)
        this.$message.error('Username or password is invalid');
      })
    }
  }
};
</script>

<style scoped>
.login {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}
.login-button {
  width: 100%;
  margin-top: 40px;
}
.login-form {
  width: 290px;
}
</style>
<style lang="scss">
$teal: rgb(0, 124, 137);
.el-button--primary {
  background: $teal;
  border-color: $teal;
  &:hover,
  &.active,
  &:focus {
    background: lighten($teal, 7);
    border-color: lighten($teal, 7);
  }
}
.login .el-input__inner:hover {
  border-color: $teal;
}
.login .el-input__prefix {
  background: rgb(238, 237, 234);
  height: calc(100% - 2px);
  top: 1px;
  border-radius: 3px;
  .el-input__icon {
    width: 30px;
  }
}
.login .el-card {
  padding-top: 0;
  padding-bottom: 30px;
}
h2 {
  letter-spacing: 1px;
  padding-bottom: 20px;
}
a {
  color: $teal;
  text-decoration: none;
  &:hover,
  &:active,
  &:focus {
    color: lighten($teal, 7);
  }
}
.login .el-card {
  width: 340px;
  display: flex;
  justify-content: center;
}
</style>
