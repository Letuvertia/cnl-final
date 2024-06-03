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
      feedIntervalId: null,
      bubbles: [],
      bubble_properties: []
    };
  },
  mounted() {
    this.startUpdatingFeed();
  },
  beforeDestroy() {
    clearInterval(this.feedIntervalId);
  },
  methods: {
    handleLocationUpdate(location) {
      this.userLocation = location;
      const msg_location = {
        userid: this.userid,
        location_latitude: this.location.latitude,
        location_longitude: this.userLocation.longitude
      };
      axios.post('/api/location', msg_location) // send location to backend, this updates msg_feed as well
      .then(
        response => {
          this.msg_feed = JSON.parse(response.data);
        }
      )
      .catch(
        error => {
          console.error('Error updating location:', error);
        }
      );
      this.msgFeedsToBubbles();
    },
    startUpdatingFeed() {
      this.feedIntervalId = setInterval(this.getFeed, 3000);
    },
    newMessage(text) {
      const msg_put = {
        userid: this.userid,
        new_msg: {
          msg_userid: this.userid,
          msg_content: text,
          msg_location_latitude: this.userLocation.latitude,
          msg_location_longitude: this.location.longitude
        }
      };
      axios.put('/api/message', msg_put) // send new message to backend
      .then()
      .catch(
        error => {
          console.error('Error updating location:', error);
        }
      );
      this.getFeed(); // send a request for msg_feed to backend
      this.msgFeedsToBubbles();
    },
    getFeed() {
      axios.get('/api/feed,', JSON.stringify({ userid : this.userid }))
      .then(
        response => {
          this.msg_feed = JSON.parse(response.data);
        }
      )
      .catch(
        error => {
          console.error('Error updating msg_feed:', error);
        }
      )
    },
    msgFeedsToBubbles() { // convert msg_feed to local bubbles
      this.bubbles = [];
      for (let i = 0; i < this.msg_feed.length; i++) {
        this.addBubble(m, i);
      }
    },
    addBubble(msg, index) {
      const bubble = {
        id: msg.msg_userid,
        content: msg.msg_content,
        likes: msg.msg_likes,
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
        msg_id: bubble.id
      }
      axios.put('/api/like', like_msg)  // send like message to backend
      .then()
      .catch(
        error => {
          console.error('Error updating location:', error);
        }
      );
      this.getFeed(); // send request for msg_feed to backend
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
