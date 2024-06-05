<script>
import { RouterLink, RouterView } from 'vue-router'

import{reactive, onMounted, toRaw} from 'vue';
import axios from 'axios';

const test_url = '/api/userdata?userid=1'

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
    
  <RouterView />
</template>
