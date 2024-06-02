<template>
  <div class="main-view">
    <UserLocation @location-updated="handleLocationUpdate" />
    <MessageInput @new-message="newMessage" />
    <Bubble 
      v-for="(bubble, index) in bubbles" 
      :key="index" 
      :text="bubble.text"
      :likes="bubble.likes" 
      :liked="bubble.liked"
      :top="bubble.top"
      :left="bubble.left"
      :color="bubble.color"
      @toggle-like="toggleLike(index)"
    />
  </div>
</template>

<script>
import MessageInput from '../components/MessageInput.vue';
import Bubble from '../components/Bubble.vue';
import UserLocation from '../components/UserLocation.vue';
import axios from 'axios';

axios.defaults.baseURL = 'http://localhost:5000';

export default {
  components: {
    MessageInput,
    Bubble,
    UserLocation
  },
  data() {
    return {
      userid: 0,
      username: '',
      userLocation: { latitude: 0, longitude: 0 },
      msg_feed: [],
      bubbles: [],
      bubble_properties: []
    };
  },
  methods: {
    handleLocationUpdate(location) { // update location and send to backend
      this.userLocation = location;
      const msg_location_json = JSON.stringify({ userid: this.userid, location: this.userLocation});
      axios.post('/api/location', msg_location_json)
      .then()
      .catch(
        error => {
          console.error('Error updating location:', error);
        }
      );
      axios.get('/api/feed,', JSON.stringify({ userid : this.userid }))
      .then(
        response => {
          this.msg_feed = JSON.parse(response.data.msg_feed);
        }
      )
      .catch(
        error => {
          console.error('Error updating msg_feed:', error);
        }
      );
      // send location message to backend
      // send request for msg_feed to backend
      this.msgFeedsToBubbles();
    },
    newMessage(text) { // send entered message to backend
      const msg_put = {
        userid: this.userid,
        new_msg: {
            msg_content: text,
            msg_location: this.userLocation,
            msg_user: this.username
        }
      };
      const msg_put_json = JSON.stringify(msg_put);
      axios.put('/api/message', msg_put_json)
      .then()
      .catch(
        error => {
          console.error('Error updating location:', error);
        }
      );
      axios.get('/api/feed,', JSON.stringify({ userid : this.userid }))
      .then(
        response => {
          this.msg_feed = JSON.parse(response.data.msg_feed);
        }
      )
      .catch(
        error => {
          console.error('Error updating msg_feed:', error);
        }
      );
      // send new message to backend
      // send a request for msg_feed to backend
      this.msgFeedsToBubbles();
    },
    msgFeedsToBubbles() { // convert msg_feed to local bubbles
      this.bubbles = [];
      for (let i = 0; i < this.msg_feed.length; i++) {
        this.addBubble(m, i);
      }
    },
    addBubble(msg, index) {
      const bubble = {
        id: msg.msg_id,
        content: msg.msg_content,
        likes: msg.msg_likes,
        location: msg.msg_location,
        user: msg.msg_user,
        liked: msg.msg_liked,
        top: this.bubble_properties[index].t,
        left: this.bubble_properties[index].l,
        color: this.bubble_properties[index].c
      }
      this.bubbles.push(bubble);
    },
    generateRandomColor() {
      const letters = '0123456789ABCDEF';
      let color = '#';
      for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
      }
      return color;
    },
    toggleLike(index) {
      const bubble = this.bubbles[index];
      const like_msg = {
        userid: this.userid,
        msg_id: bubble.id,
        liked: !bubble.liked
      }
      const msg_like_json = JSON.stringify(like_msg);
      axios.put('/api/like', msg_like_json)
      .then()
      .catch(
        error => {
          console.error('Error updating location:', error);
        }
      );
      axios.get('/api/feed,', JSON.stringify({ userid : this.userid }))
      .then(
        response => {
          this.msg_feed = JSON.parse(response.data.msg_feed);
        }
      )
      .catch(
        error => {
          console.error('Error updating msg_feed:', error);
        }
      );
      // send like message to backend
      // send request for msg_feed to backend
      this.msgFeedsToBubbles();
    },
    generateRandomProperties() {
      for (let i = 0; i < 100; i++) {
        this.bubble_properties.push({
          t: Math.random() * (window.innerHeight - 200) + 50,
          l: Math.random() * (window.innerWidth - 150) + 25,
          c: this.generateRandomColor()
        });
      }
    }
  }
};
</script>

<style scoped>
.main-view {
  position: relative;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
}
</style>
