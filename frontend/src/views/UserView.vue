<template>
    <div>
        <div v-if="user">
            <h1>{{ user.username }}'s Messages</h1>
            <table class="message-table">
                <tbody>
                    <tr v-for="message in filteredMessages" :key="message.msg_id">
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
            /* messages: [
                {
                    "msg_id": "0",
                    "msg_content": "計網實 4 顆星",
                    "msg_likes": "2",
                    "msg_location": "",
                    "msg_user": "grace"
                },
                {
                    "msg_id": "1",
                    "msg_content": "CNL sucks!",
                    "msg_likes": "3",
                    "msg_location": "",
                    "msg_user": "grace"
                },
                {
                    "msg_id": "2",
                    "msg_content": "Hello",
                    "msg_likes": "1",
                    "msg_location": "",
                    "msg_user": "john"
                },
            ], */
        };
    },
    computed: {
        filteredMessages() {
            if (this.user) {
                return this.messages.filter(message => message.msg_user === this.user.username);
            }
            return [];
        }
    },
    mounted() {
        this.loadUserData();
        this.loadMessages();
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
        loadMessages() {
            const msgFeed = localStorage.getItem('msgFeed');
            if (msgFeed) {
                this.messages = JSON.parse(msgFeed);
            }
        },
        async fetchMessages() {
            try {
                const response = await axios.get('/feed');
                this.messages = response.data;
            } catch (error) {
                console.error('Error fetching messages:', error);
            } finally {
                this.loading = false;
            }
        }
    },
};
</script>
