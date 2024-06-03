<template>
    <div>
        <div v-if="user">
            <h1>{{ user }}'s Messages</h1>
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
                    console.log('userid:', userid, ', username:', this.user);
                    // Make API call to get userdata
                    console.log('Trying to call API');
                    const response = await axios.get('/api/userdata', {
                        params: {
                            userid: userid,
                        }
                    });
                    console.log('API response got.');
                    if (response.status === 200) {
                        this.messages = response.data.msg_history;
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
