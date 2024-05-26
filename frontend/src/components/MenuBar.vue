<template>
  <div>
    <button @click="toggleMenu" class="menu-button">
      &#9776;
    </button>
    <div v-if="menuVisible" class="menu">
      <ul>
        <li @click="goToUserPage">User Page</li>
        <li @click="goToMain">Main</li>
        <li @click="goToLoginPage">Log out</li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      menuVisible: false
    };
  },
  methods: {
    toggleMenu() {
      this.menuVisible = !this.menuVisible;
    },
    goToUserPage() {
      this.$emit('navigate', 'UserPage');
      this.menuVisible = false;
    },
    goToLoginPage() {
      this.$emit('navigate', 'LoginPage');
      this.menuVisible = false;
    },
    goToMain() {
      this.$emit('navigate', 'Main');
      this.menuVisible = false;
    },
  }
};
</script>

<style scoped>
.menu-button {
  position: absolute;
  top: 10px;
  left: 10px;
  font-size: 24px;
  cursor: pointer;
}

.menu {
  position: absolute;
  top: 50px;
  left: 10px;
  width: 200px;
  background-color: white;
  box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
  z-index: 1000;
}

ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

li {
  padding: 10px;
  cursor: pointer;
}

li:hover {
  background-color: #f0f0f0;
}
</style>
