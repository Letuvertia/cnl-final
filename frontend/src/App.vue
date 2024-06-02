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
          <RouterLink to="/main" class="nav-link">Main</RouterLink>
          <RouterLink to="/user" class="nav-link">User</RouterLink>
          <RouterLink to="/login" class="nav-link">Log Out</RouterLink>
        </nav>
      </div>
    </header>
  <RouterView />
</template>
