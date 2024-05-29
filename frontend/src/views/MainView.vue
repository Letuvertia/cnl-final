<template>
  <div class="main-view">
    <MessageInput @new-bubble="addBubble" />
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

export default {
  components: {
    MessageInput,
    Bubble
  },
  data() {
    return {
      bubbles: []
    };
  },
  methods: {
    addBubble(text) {
      const t = Math.random() * (window.innerHeight - 200) + 50;
      const l = Math.random() * (window.innerWidth - 150) + 25;
      const c = this.generateRandomColor()
      this.bubbles.push({ text, likes: 0, liked: false, top: t, left: l, color: c});
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
      bubble.liked = !bubble.liked;
      if (bubble.liked) {
        bubble.likes++;
        bubble.size
      }
      else {
        bubble.likes--;
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
