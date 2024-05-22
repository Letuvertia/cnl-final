<script>
import { RouterLink, RouterView } from 'vue-router'

import{reactive, onMounted, toRaw} from 'vue';
import axios from 'axios';

const test_url = '/api/userdata?uid=123'

export default {
    setup() {
        const data = reactive({
            newsdata:'',
        })
        onMounted(() => {
            console.log(`Try to access Flask backend api: ${test_url}`)
            axios.get(test_url).then((res)=>{
              console.log(res.data)
              data.newsdata = res
            })
        });
    return {data};
   },
}
</script>

<template>
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
    <HelloWorld msg="You did it!" />
  <RouterView />
</template>
