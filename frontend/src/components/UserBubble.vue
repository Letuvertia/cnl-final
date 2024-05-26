<template>
  <div class="user-bubble">
    <p>{{ displayText }}</p>
  </div>
  <div class="input-container">
    <input v-model="inputText" @keydown.enter="updateText" type="text" placeholder="Enter text here" />
    <button @click="updateText">Enter</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      inputText: '',
      displayText: 'Your text here',
      textHistory: []
    };
  },
  methods: {
    updateText() {
      if (this.inputText.trim() !== '') {
        this.displayText = this.inputText;
        this.$emit('update-history', this.inputText);
        this.inputText = '';
      }
    }
  }
};
</script>

<style scoped>

.user-bubble {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  background-color: #3498db;
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
  font-size: 16px;
  text-align: center;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

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

ul {
  list-style: none;
  padding: 0;
}

li {
  background: #f0f0f0;
  margin: 5px 0;
  padding: 10px;
  border-radius: 5px;
}
</style>
