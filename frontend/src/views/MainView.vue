<template>
  <div class="main-view">
    <UserLocation @location-updated="handleLocationUpdate" />
    <MessageInput @new-message="newMessage" />
    <Bubble 
      v-for="(bubble, index) in bubbles" 
      :key="index"
      :id="bubble.id"
      :content="bubble.content"
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
    this.userid = JSON.parse(localStorage.getItem('userData')).userid;
    this.username = JSON.parse(localStorage.getItem('userData')).username;
    this.generateRandomProperties();
    this.startUpdatingFeed();
  },
  beforeDestroy() {
    console.log("stop feeding", this.userid);
    clearInterval(this.feedIntervalId);
  },
  methods: {
    handleLocationUpdate(location) {
      this.userLocation = location;
      axios.post('/api/location', {
          userid: this.userid,
          location_latitude: this.userLocation.latitude,
          location_longitude: this.userLocation.longitude
        })
        .then(response => {
          this.msg_feed = response.data;
        })
        .catch(error => {
          console.error('Error updating location:', error);
        });
    },
    startUpdatingFeed() {
      this.feedIntervalId = setInterval(this.getFeed, 3000);
    },
    newMessage(text) {
      axios.put('/api/message', {
          userid: this.userid,
          new_msg: {
            msg_userid: this.userid,
            msg_content: text,
            msg_location_latitude: this.userLocation.latitude,
            msg_location_longitude: this.userLocation.longitude
          }
        })
        .then()
        .catch(error => {
          console.error('Error adding a new message :', error);
        });
      this.getFeed();
    },
    getFeed() {
      axios.get(`/api/feed?userid=${this.userid}`)
        .then(response => {
          this.msg_feed = response.data;
        })
        .catch(error => {
          console.error('Error updating feed:', error);
        });
      this.msg_feed.sort((a, b) => a.msg_id - b.msg_id);
      this.msgFeedsToBubbles();
    },
    msgFeedsToBubbles() {
      this.bubbles = [];
      for (let i = 0; i < this.msg_feed.length; i++) {
        let msg = this.msg_feed[i];
        this.bubbles.push(
          {
            id: msg.msg_id,
            content: msg.msg_content,
            likes: msg.msg_likes,
            liked: msg.msg_liked,
            top: this.bubble_properties[i].t,
            left: this.bubble_properties[i].l,
            color: this.bubble_properties[i].c
          }
        );
      }
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
      axios.put('/api/like', {
          userid: this.userid,
          msg_id: bubble.id
        })
        .then()
        .catch(error => {
          console.error('Error updating location:', error);
        });
      this.getFeed();
    },
    generateRandomProperties() {
      this.bubble_properties = [];
      const maxAttempts = 1000;
      for (let i = 0; i < 50; i++) {
        let attempts = 0;
        let overlapping = true;
        let property;
        while (overlapping && attempts < maxAttempts) {
          property = {
            t: Math.random() * (window.innerHeight - 200) + 50,
            l: Math.random() * (window.innerWidth - 150) + 25,
            c: this.generateRandomColor()
          };
          overlapping = this.checkOverlap(property);
          attempts++;
        }
        if (!overlapping) {
          this.bubble_properties.push(property);
        }
      }
    },
    checkOverlap(newProperty) {
      for (const property of this.bubble_properties) {
        const dx = newProperty.l - property.l;
        const dy = newProperty.t - property.t;
        if (dx * dx + dy * dy < 18000) {
          return true;
        }
      }
      return false;
    }
  },
  beforeRouteLeave(to, from, next) {
    clearInterval(this.feedIntervalId);
    next();
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
