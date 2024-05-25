<template>
    <div class="container m-5">
        <form @submit.prevent="userRegistration">
            <h1>Register</h1>
            <div class="form-group">
                <label>Name &nbsp</label>
                <input
                type="text"
                class="form-control form-control-lg"
                v-model="user.name"
                />
            </div>
        
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
            <button type="submit" class="btn btn-dark btn-lg btn-block">
                Register
            </button>
        
            <p class="text-right">
                Already registered?
                <router-link to="/login">Login</router-link>
            </p>
        </form>
    </div>
</template>
  

<script>
export default {
    data() {
        return {
            user: {
                name: "", 
                email: "",
                password: "",
            },
            user_db: {},
        };
    },
    methods: {
        userRegistration() {
            this.createUserWithEmailAndPassword(this.user.email, this.user.password)
            .then(() => {
                this.$router.push("/login");
            })
            .catch((error) => {
                alert(error.message);
            });
        },
        createUserWithEmailAndPassword(email, password) {
            this.user_db[email] = password;
        },
    },
};
</script>
