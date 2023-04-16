<template>
  <div id="app">
    <EventList />
  </div>
</template>

<script>

import EventList from './components/EventList.vue';



export default {
  name: 'App',
  components: {

    EventList
  }
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
