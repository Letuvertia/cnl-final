<template>
    <div class="container m-5">
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
                const response = await axios.post('/login', {
                    username: this.user.username,
                    password: this.user.password,
                });

                if (response.data.auth_status === 'success') {
                    const userData = response.data.data.userdata;
                    const msgFeed = response.data.data.msg_feed;

                    localStorage.setItem('authToken', this.userLogin.username); // Store token in localStorage
                    localStorage.setItem('loginTime', new Date().getTime()); // Store login time
                    localStorage.setItem('userData', JSON.stringify(userData));
                    localStorage.setItem('msgFeed', JSON.stringify(msgFeed));

                    this.$router.push("/main");
                } else {
                    alert("Login failed. Please check your credentials.");
                }
            } catch (error) {
                alert('An error occurred: ' + error.message);
            }
            /*const email = this.user.email;
            const password = this.user.password;
            if (this.login_check(email, password)) {
                localStorage.setItem('authToken', email); // Store token in localStorage
                localStorage.setItem('loginTime', new Date().getTime()); // Store login time
                this.$router.push("/user"); // Redirect to user page
            } else {
                alert("Invalid email or password.");
            }*/
        },
        login_check(email, password) {
            return email in this.user_db && this.user_db[email] === password;
        },
    },
};
</script>
