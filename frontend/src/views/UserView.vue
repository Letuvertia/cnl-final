<template>
    <header class="nav-bar">
      <div class="wrapper">
        <nav>
          <RouterLink to="/main" class="nav-link">Main</RouterLink>
          <RouterLink to="/user" class="nav-link">User</RouterLink>
          <RouterLink to="/login" class="nav-link">Log Out</RouterLink>
        </nav>
      </div>
    </header>
    <div>
        <div v-if="user" class="content">
            <h1> {{ user }}'s page </h1>
            <br>
            <h2> Info </h2>
            <p> 📧 {{ data.email }}</p>
            <p> 📍 ({{ data.location_latitude }}, {{ data.location_longitude }})</p>
            <br>
            <h2> Messages </h2>
            <table class="message-table">
                <tbody>
                    <tr v-for="message in messages" :key="message.msg_id">
                        <td>{{ message.msg_content }}</td>
                        <td class="likes-cell">
                            <i>♡ &nbsp</i>
                            <span>{{ message.msg_likes }}</span>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div v-else>
            <p>Loading...</p>
        </div>
    </div>
</template>
  
<script>

import axios from 'axios';

export default {
    data() {
        return {
            user: null,
            messages: [],
            data: {},
            loading: true,
        };
    },
    mounted() {
        this.loadUserData();
        this.loading = false;
    },
    methods: {
        async loadUserData() {
            try {
                const userData = localStorage.getItem('userData');
                if (userData) {
                    const parsedUserData = JSON.parse(userData);
                    this.user = parsedUserData.username;
                    const userid = parsedUserData.userid;
                    // Make API call to get userdata
                    const response = await axios.get('/api/userdata', {
                        params: {
                            userid: userid,
                        }
                    });
                    if (response.status === 200) {
                        this.messages = response.data.msg_history;
                        this.data = response.data;
                    } else {
                        alert('Failed to load user data');
                        this.$router.push('/login');
                    }
                } else {
                    this.$router.push('/login');
                }
            } catch (error) {
                console.error('An error occurred:', error.message);
                this.$router.push('/login');
            }
        },
    },
};
</script>

<style scoped>
.content {
  margin-top: 70px; /* Adjust this value if your header's height changes */
  padding: 1rem;
}
</style>
