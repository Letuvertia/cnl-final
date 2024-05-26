<script setup>
import { useRouter } from 'vue-router';
import { ref, onMounted } from 'vue';

const router = useRouter();
const isAuthenticated = ref(false); // This should be replaced with your actual auth check

// Simulate a method to check if the user is authenticated
function checkAuthentication() {
  const authToken = localStorage.getItem('authToken');
  const loginTime = localStorage.getItem('loginTime');
  const currentTime = new Date().getTime();
  const sessionTimeout = 30 * 60 * 1000; // 30 minutes

  if (authToken && loginTime && (currentTime - loginTime) < sessionTimeout) {
    return true;
  } else {
    localStorage.removeItem('authToken');
    localStorage.removeItem('loginTime');
    return false;
  }
}

onMounted(() => {
  isAuthenticated.value = checkAuthentication();

  if (isAuthenticated.value) {
    router.push('/user'); // Redirect to user view if authenticated
  } else {
    router.push('/login'); // Redirect to login view if not authenticated
  }
});

</script>

<template>
  <main>
    <p>Loading...</p>
  </main>
</template>
