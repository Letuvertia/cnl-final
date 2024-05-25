<template>
    <div class="container m-5">
        <form @submit.prevent="userLogin">
            <h1>Login</h1>
            <div class="form-group">
                <label>Email &nbsp</label>
                <input
                    type="email"
                    class="form-control form-control-lg"
                    v-model="user.email"
                />
            </div>
            <div class="form-group">
                <label>Password &nbsp</label>
                <input
                    type="password"
                    class="form-control form-control-lg"
                    v-model="user.password"
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
export default {
    data() {
        return {
            user: {
                email: "",
                password: "",
            },
            user_db: {'grace@gmail.com': 'pw'},
        };
    },
    methods: {
        userLogin() {
            const email = this.user.email;
            const password = this.user.password;
            if (this.login_check(email, password)) {
                localStorage.setItem('authToken', email); // Store token in localStorage
                localStorage.setItem('loginTime', new Date().getTime()); // Store login time
                this.$router.push("/user"); // Redirect to user page
            } else {
                alert("Invalid email or password.");
            }
        },
        login_check(email, password) {
            return email in this.user_db && this.user_db[email] === password;
        },
    },
};
</script>
