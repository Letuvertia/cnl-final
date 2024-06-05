<template>
   <div class="input-container">
    <input v-model="inputLatitude" type="number" placeholder="Enter latitude" />
    <input v-model="inputLongitude" type="number" placeholder="Enter longitude" />
    <button @click="updateManualLocation">Update Location</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      userLocation: { latitude: 0, longitude: 0 },
      inputLatitude: 0,
      inputLongitude: 0
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
      this.$emit('location-updated', this.userLocation);
    },
    updateManualLocation() {
      if (this.inputLatitude && this.inputLongitude) {
        this.userLocation = {
          latitude: parseFloat(this.inputLatitude),
          longitude: parseFloat(this.inputLongitude)
        };
      }
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
