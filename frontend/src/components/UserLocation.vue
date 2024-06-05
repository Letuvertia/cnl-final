<template>
   <div class="input-container">
    <input v-model="inputLatitude" type="text" placeholder="Enter latitude" />
    <input v-model="inputLongitude" type="text" placeholder="Enter longitude" />
    <button @click="updateManualLocation">Update Location</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      userLocation: { latitude: 0, longitude: 0 },
      inputLatitude: '',
      inputLongitude: ''
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
      if (this.inputLatitude != '' && this.inputLongitude != '') {
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
.input-container {
  position: absolute;
  bottom: 10px;
  right: 10px;
  background-color: rgba(0, 0, 0, 0.5);
  color: #fff;
  padding: 10px;
  border-radius: 5px;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}

input {
  margin-bottom: 5px;
  padding: 5px;
  border-radius: 3px;
  border: 1px solid #ccc;
}

button {
  padding: 5px 10px;
  border: none;
  border-radius: 3px;
  background-color: #3498db;
  color: white;
  cursor: pointer;
}
</style>
