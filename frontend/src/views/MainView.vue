<template>
  <div id="app">
    <MenuBar @navigate="handleNavigation" />
    <UserLocation @location-updated="updateUserLocation" />
    <router-view :textHistory="textHistory" @update-history="updateTextHistory" :userLocation="userLocation" />
    <UserBubble />
  </div>
</template>

<script>
import MenuBar from '../components/MenuBar.vue';
import UserLocation from '../components/UserLocation.vue';
import UserBubble from '../components/UserBubble.vue';

export default {
  components: {
    UserLocation,
    UserBubble,
    MenuBar,
  },
  data() {
    return {
      textHistory: [], // Store the history of texts
      userLocation: { latitude: 0, longitude: 0 } // Store the user's location
    };
  },
  methods: {
    handleNavigation(page) {
      if (page === 'UserPage') {
        this.$router.push({ name: 'UserPage', params: { textHistory: this.textHistory } });
      }
      else if (page === 'LoginPage') {
        // TODO
      }
      else if (page === 'Main') {
        this.$router.push({ name: 'Main' });
      }
    },
    updateTextHistory(newText) {
      this.textHistory.unshift(newText);
    },
    updateUserLocation(location) {
      this.userLocation = location;
    }
  }
};
</script>

<style>
/* Your other styles */
</style>
