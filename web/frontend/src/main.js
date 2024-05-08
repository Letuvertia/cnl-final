import { createApp } from 'vue';

const app = createApp({
  template: `<h1>Hello, {{ name }}!</h1>`,
  data() {
    return {
      name: 'World',
    }
  }
});

app.mount('#app');
