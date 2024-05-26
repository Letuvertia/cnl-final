<template>
  <div class="location-display">
    Latitude: {{ userLocation.latitude }}, Longitude: {{ userLocation.longitude }}
  </div>
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
    this.locationInterval = setInterval(this.updateLocation, 5000);
  },
  beforeDestroy() {
    clearInterval(this.locationInterval);
  },
  methods: {
    updateLocation() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(this.showPosition, this.showError);
      } else {
        console.log("Geolocation is not supported by this browser.");
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
.location-display {
  position: absolute;
  bottom: 10px;
  right: 10px;
  background-color: rgba(0, 0, 0, 0.5);
  color: #fff;
  padding: 5px 10px;
  border-radius: 5px;
}
</style>
