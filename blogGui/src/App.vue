<template>
  <div class="navbar">
    <a class="goBack" href="addPost.html">Make a post</a>
    <a class="goBack" href="addPost.html">CreateAccount</a>
  </div>
  <allBlogs />
</template>

<script>
import allBlogs from './components/allBlogs.vue'

export default {
  components: {
    allBlogs
  }
}
</script>

<style>
:root {
  --paddingX: 50px;
  --paddingY: 7px;
}

.navbar {
  height: 60px;
  padding: 8px;
  display: flex;
  justify-content: center;
  background-color: #285430;
  align-items: center;
}

.navbar > a{
  --mrgs:15px;
  margin-right: var(--mrgs);
  margin-left: var(--mrgs);
}

.goBack {
  height: 21px;
  text-decoration: none;
  color: rgb(98, 98, 98);
  background-color: white;
  border: 2px rgba(151, 151, 151, 0.635) solid;
  border-radius: 5px;
  padding: var(--paddingY) var(--paddingX) var(--paddingY) var(--paddingX);
  transition: 0.5s;
  
}

.goBack:hover {
  /* transition-delay: 0.3s; */

  color: azure;
  background-color: rgba(128, 128, 128, 0.648);
  border-color: rgba(128, 128, 128, 0.648);
  padding: calc(var(--paddingY) + 7px) calc(var(--paddingX) + 7px) calc(var(--paddingY) + 7px) calc(var(--paddingX) + 7px);
  font-size: 117%;

}
</style>