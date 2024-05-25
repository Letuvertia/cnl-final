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
            this.login_check(this.user.email, this.user.password)
            .then(() => {
                this.$router.push("/");
            })
            .catch((error) => {
                alert(error.message);
            });
        },
        login_check(email, password) {
            if (!(email in this.user_db) || user_db[email] !== password) {
                return false;
            } else {
                return true;
            }
        },
    },
};
</script>
