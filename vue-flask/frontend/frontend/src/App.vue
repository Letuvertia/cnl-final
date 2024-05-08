<template>
  <div id="app">
    <h1>Registration</h1>
    <div>
      <input type="text" placeholder="Username" v-model="registerData.username">
      <input type="password" placeholder="Password" v-model="registerData.password">
      <button @click="register">Register</button>
    </div>
    <h1>Login</h1>
    <div>
      <input type="text" placeholder="Username" v-model="loginData.username">
      <input type="password" placeholder="Password" v-model="loginData.password">
      <button @click="login">Login</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      registerData: {
        username: '',
        password: ''
      },
      loginData: {
        username: '',
        password: ''
      }
    };
  },
  methods: {
    register() {
      axios.post('http://localhost:5000/register', this.registerData)
        .then(response => {
          console.log(response.data.message);
          this.registerData.username = '';
          this.registerData.password = '';
        })
        .catch(error => {
          console.error(error.response.data.message);
        });
    },
    login() {
      axios.post('http://localhost:5000/login', this.loginData)
        .then(response => {
          console.log(response.data.message);
          this.loginData.username = '';
          this.loginData.password = '';
        })
        .catch(error => {
          console.error(error.response.data.message);
        });
    }
  }
};
</script>

<style>
#app {
  text-align: center;
  margin-top: 50px;
}
input {
  margin-bottom: 10px;
}
button {
  margin-top: 10px;
}
</style>
