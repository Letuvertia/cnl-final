<template>
    <div>
        <div v-if="user">
            <h1>{{ user.username }}'s Messages</h1>
            <table class="message-table">
                <tbody>
                    <tr v-for="message in user.msg_history" :key="message.msg_id">
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
            loading: true,
        };
    },
    mounted() {
        this.loadUserData();
        this.loading = false;
    },
    methods: {
        loadUserData() {
            const userData = localStorage.getItem('userData');
            if (userData) {
                this.user = JSON.parse(userData);
            } else {
                this.$router.push('/login');
            }
        },
    },
};
</script>
