<template>
  <div :class="['bubble', randomClass]" :style="bubbleStyle" @click="toggleLike">
    <p>{{ text }}</p>
    <p>♡ &nbsp {{ likes }}</p>
  </div>
</template>

<script>
export default {
  props: {
    id: {
      type: Number,
      required: true
    },
    content: {
      type: String,
      required: true
    },
    likes: {
      type: Number,
      required: true
    },
    liked: {
      type: Boolean,
      required: true
    },
    top: {
      type: Number,
      default: 0
    },
    left: {
      type: Number,
      default: 0
    },
    color: {
      type: String,
      default: 0
    }
  },
  computed: {
    bubbleStyle() {
      const size = 100 + this.likes * 20;
      return {
        width: `${size}px`,
        height: `${size}px`,
        position: 'absolute',
        top: `${this.top - size / 2}px`,
        left: `${this.left - size / 2}px`,
        backgroundColor: this.color
      };
    }
  },
  methods: {
    toggleLike() {
      this.$emit('toggle-like', !this.liked);
    }
  }
};
</script>

<style scoped>
.bubble {
  border-radius: 50%;
  background-color: #3498db;
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
  font-size: 16px;
  text-align: center;
  flex-direction: column;
  cursor: pointer;
}
</style>
