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
                required
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
                required
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
import axios from 'axios';

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
        async userRegistration() {
            try {
                const response = await axios.post('/register', {
                    username: this.user.username,
                    email: this.user.email,
                    password: this.user.password
                });

                if (response.data.register_status === 'success') {
                    this.$router.push('/login');
                } else {
                    alert('Registration failed. Please try again.');
                }
            } catch (error) {
                alert('An error occurred: ' + error.message);
            }
            /*this.createUserWithEmailAndPassword(this.user.email, this.user.password)
            .then(() => {
                this.$router.push("/login");
            })
            .catch((error) => {
                alert(error.message);
            });*/
        },
        createUserWithEmailAndPassword(email, password) {
            this.user_db[email] = password;
        },
    },
};
</script>
