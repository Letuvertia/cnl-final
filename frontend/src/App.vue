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
  <header>
    <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="You did it!" />

      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>