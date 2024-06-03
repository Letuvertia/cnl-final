<template>
  <!-- No content to display -->
</template>

<script>
export default {
  data() {
    return {
      userLocation: { latitude: 0, longitude: 0 }
    };
  },
  mounted() {
    this.updateLocation();
    this.locationInterval = setInterval(this.updateLocation, 60000);
  },
  beforeDestroy() {
    clearInterval(this.locationInterval);
  },
  methods: {
    updateLocation() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(this.showPosition, this.showError);
      }
      else {
        console.log('Geolocation is not supported by this browser.');
      }
    },
    showPosition(position) {
      this.userLocation = {
        latitude: position.coords.latitude,
        longitude: position.coords.longitude
      };
      this.$emit('location-updated', this.userLocation);
    },
    showError(error) {
      console.error(error);
    }
  }
};
</script>

<style scoped>
/* No styles needed */
</style>
