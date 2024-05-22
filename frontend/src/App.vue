<template>
  <div>
    <header class="nav-bar">
      <div class="wrapper">

        <nav>
          <RouterLink to="/" class="nav-link">Home</RouterLink>
          <RouterLink to="/about" class="nav-link">About</RouterLink>
          <RouterLink to="/login" class="nav-link">Login</RouterLink>
          <RouterLink to="/register" class="nav-link">Register</RouterLink>
        </nav>
      </div>
    </header>

    <main class="content">
      <router-view />
    </main>
  </div>
</template>

<script>
import { RouterLink } from 'vue-router'

export default {
  components: {
    RouterLink
  }
}
</script>