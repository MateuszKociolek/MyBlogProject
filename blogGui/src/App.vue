<template>
  <h3>Hello Vue!</h3>
  <a href="addPost.html">Goto</a>
  <allBlogs/>
</template>

<script>
  import allBlogs from './components/allBlogs.vue'

  export default {
      components:{
        allBlogs
      }
  }
</script>

<style>

</style>