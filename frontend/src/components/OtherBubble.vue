<template>
  <div v-if="isWithinDistance" class="bubble" :style="bubbleStyle" @click="incrementLikes">
    <p>{{ text }}</p>
    <p>Likes: {{ likes }}</p>
  </div>
</template>

<script>
export default {
  props: {
    id: Number,
    text: String,
    location: Object, // { latitude: Number, longitude: Number }
    likes: Number,
    userLocation: Object // { latitude: Number, longitude: Number }
  },
  data() {
    return {
      localLikes: this.likes
    };
  },
  computed: {
    bubbleStyle() {
      return {
        width: `${this.localLikes}px`,
        height: `${this.localLikes}px`,
        borderRadius: '50%',
        backgroundColor: '#3498db',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        color: 'white',
        fontSize: '16px',
        textAlign: 'center',
        position: 'absolute',
        top: `${this.location.top}`,
        left: `${this.location.left}`,
        transform: 'translate(-50%, -50%)',
        cursor: 'pointer'
      };
    },
    isWithinDistance() {
      return this.calculateDistance(
        this.userLocation.latitude,
        this.userLocation.longitude,
        this.location.latitude,
        this.location.longitude
      ) <= 500;
    }
  },
  methods: {
    incrementLikes() {
      this.localLikes += 1;
      this.$emit('update-likes', this.localLikes, this.location);
    },
    calculateDistance(lat1, lon1, lat2, lon2) {
      const R = 6371000; // radius of Earth in meters
      const toRad = x => (x * Math.PI) / 180;
      const dLat = toRad(lat2 - lat1);
      const dLon = toRad(lon2 - lon1);
      const a =
        Math.sin(dLat / 2) * Math.sin(dLat / 2) +
        Math.cos(toRad(lat1)) * Math.cos(toRad(lat2)) *
        Math.sin(dLon / 2) * Math.sin(dLon / 2);
      const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
      return R * c; // distance in meters
    }
  },
  watch: {
    likes(newLikes) {
      this.localLikes = newLikes;
    }
  }
};
</script>

<style scoped>
.bubble {
  position: absolute;
}
</style>
