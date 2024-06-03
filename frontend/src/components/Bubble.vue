<template>
  <div :class="['bubble']" :style="bubbleStyle" @click="toggleLike">
    <p class="bubble-text">{{ content }}</p>
    <p class="bubble-likes">Likes: {{ likes }}</p>
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
      const size = 150 + this.likes * 20;
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
      this.$emit('toggle-like');
    }
  }
};
</script>

<style scoped>
.bubble {
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  cursor: pointer;
  color: white;
  font-size: 16px;
  text-align: center;
  position: relative;
}

.bubble-text {
  margin: 0;
}

.bubble-likes {
  margin: 0;
  font-size: 12px;
  position: absolute;
  bottom: 10px;
}
</style>
