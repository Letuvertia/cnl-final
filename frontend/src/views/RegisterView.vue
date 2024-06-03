<template>
    <div class="container m-5">
        <form>
            <h1>Register</h1>
            <div class="form-group">
                <label>Name &nbsp</label>
                <input
                type="text"
                class="form-control form-control-lg"
                v-model="user.username"
                required
                />
            </div>
        
            <div class="form-group">
                <label>Email &nbsp</label>
                <input
                type="email"
                class="form-control form-control-lg"
                v-model="user.email"
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
            <button type="button" class="btn btn-dark btn-lg btn-block" @click="userRegistration">
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
        };
    },
    methods: {
        async userRegistration() {
            try {
                const response = await axios.post('/api/register', {
                    username: this.user.username,
                    password: this.user.password,
                    email: this.user.email,
                });
                if (response.data.register_status === 'success') {
                    this.$router.push('/login');
                } else {
                    alert('Registration failed. Please try again.');
                }
            } catch (error) {
                alert('An error occurred: ' + error.message);
            }
        },
    },
};
</script>
