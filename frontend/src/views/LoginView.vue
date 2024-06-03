<template>
    <div style="width: 100vw; height: 100vh; position: fixed; left:0px; top:0px; z-index: 1001; background-color: white;"></div>
    <div class="container m-5" style="z-index: 1002;">
        <form @submit.prevent="userLogin">
            <h1>Login</h1>
            <div class="form-group">
                <label>Username &nbsp</label>
                <input
                    type="text"
                    class="form-control form-control-lg"
                    v-model="user.username"
                    required
                />
            </div>
            <div class="form-group">
                <label>Password &nbsp</label>
                <input
                    type="password"
                    class="form-control form-control-lg"
                    v-model="user.password"
                    required
                />
            </div>
            <button type="submit" class="btn btn-dark btn-lg btn-block">Login</button>
            <p class="text-right mt-2 mb-4">
                <RouterLink to="/register">Register</RouterLink>
            </p>
        </form>
    </div>
</template>
  
<script>
import axios from 'axios';
export default {
    data() {
        return {
            user: {
                username: "",
                password: "",
            },
        };
    },
    methods: {
        async userLogin() {
            try {
                const response = await axios.post('/api/login', {
                    username: this.user.username,
                    password: this.user.password,
                });

                if (response.data.auth_status === 'success') {
                    const userData = response.data.userdata;

                    localStorage.setItem('authToken', this.userLogin.username); // Store token in localStorage
                    localStorage.setItem('loginTime', new Date().getTime()); // Store login time
                    localStorage.setItem('userData', JSON.stringify(userData));

                    this.$router.push("/main");
                } else {
                    alert("Login failed. Please check your credentials.");
                }
            } catch (error) {
                alert('An error occurred: ' + error.message);
            }
        },
        login_check(email, password) {
            return email in this.user_db && this.user_db[email] === password;
        },
    },
};
</script>
