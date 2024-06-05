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
    router.push('/main'); // Redirect to main view if authenticated
  } else {
    router.push('/login'); // Redirect to login view if not authenticated
  }
});

</script>

<template>
  <header class="nav-bar">
      <div class="wrapper">
        <nav>
          <RouterLink to="/main" class="nav-link">Main</RouterLink>
          <RouterLink to="/user" class="nav-link">User</RouterLink>
          <RouterLink to="/login" class="nav-link">Log Out</RouterLink>
        </nav>
      </div>
    </header>
  <main>
    <p>Loading...</p>
  </main>
</template>
