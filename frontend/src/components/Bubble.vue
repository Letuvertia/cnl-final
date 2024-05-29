<template>
  <div :class="['bubble', randomClass]" :style="bubbleStyle" @click="toggleLike">
    <p>{{ text }}</p>
    <p>Likes: {{ likes }}</p>
  </div>
</template>

<script>
export default {
  props: {
    text: {
      type: String,
      required: true
    },
    likes: {
      type: Number,
      required: true
    },
    liked: {
      type: Boolean,
      default: false
    },
    top: {
      type: Number,
      required: true
    },
    left: {
      type: Number,
      required: true
    },
    color: {
      type: String,
      required: true
    }
  },
  computed: {
    bubbleStyle() {
      const size = 100 + this.likes * 20;
      return {
        width: `${size}px`,
        height: `${size}px`,
        position: 'absolute',
        top: `${this.top}px`,
        left: `${this.left}px`,
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
