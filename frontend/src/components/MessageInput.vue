<template>
  <div class="input-container">
    <input
      v-model="inputText"
      type="text"
      placeholder="Enter text here"
      @keyup.enter="handleEnter"
      @compositionstart="isComposing = true"
      @compositionend="handleComposition"
    />
    <button @click="emitMessage">Enter</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      inputText: '',
      isComposing: false
    };
  },
  methods: {
    handleEnter() {
      if (!this.isComposing) {
        this.emitMessage();
      }
    },
    handleComposition() {
      this.isComposing = false;
    },
    emitMessage() {
      if (this.inputText.trim() !== '') {
        this.$emit('new-message', this.inputText);
        this.inputText = '';
      }
    }
  }
};
</script>

<style scoped>
.input-container {
  position: absolute;
  bottom: 5%;
  left: 5%;
  display: flex;
}

input {
  width: 40vw;
  padding: 10px;
  font-size: 16px;
  box-sizing: border-box;
}

input::placeholder {
  font-style: italic;
}

button {
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  margin-left: 10px;
}
</style>
