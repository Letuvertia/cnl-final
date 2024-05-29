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
      bubbles: [],
      bubble_properties: []
    };
  },
  methods: {
    handleLocationUpdate(location) { // update location and send to backend
      this.userLocation = location;
      return JSON.stringify({ userid: this.userid, location: this.userLocation})
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
      // send new msg to backend
      // send a request for msg_feed to backend
      const msg_put_json = JSON.stringify(msg_put);
      return msg_put_json;
    },
    msgFeedsToBubbles(msg_feed_json) { // convert msg_feed from backend to local bubbles
      const msg_feed = JSON.parse(msg_feed_json);
      this.bubbles = [];
      for (let i = 0; i < msg_feed.length; i++) {
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
      // send like message to backend
      // send request for msg_feed to backend
      return JSON.stringify(like_msg);
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
