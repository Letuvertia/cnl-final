<script>
import { RouterLink, RouterView } from 'vue-router'
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
  <RouterView />
</template>
