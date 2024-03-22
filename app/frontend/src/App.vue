<template>
  <div id="container">
    <SideBar />
    <div id="content">
      <GlobalHeader />
      <TravelCalc />
    </div>
  </div>
</template>

<script>
import GlobalHeader from './components/global/GlobalHeader.vue';
import SideBar from './components/global/SideBar.vue'
import TravelCalc from './components/travelCalc/TravelCalc.vue'

export default {
  name: 'App',
  components: {
    SideBar,
    GlobalHeader,
    TravelCalc
  }
}
</script>

<style>
html,
body {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100vh;
}

:root {
  --background-grey-color: rgba(128, 128, 128, 0.432);
  --background-blue-color: #262a3b;
  --background-btn-blue: rgb(84, 164, 230);
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  width: 100%;
}

#container {
  display: flex;
  width: 100%;
}

#content {
  width: 100%;
  display: flex;
  flex-direction: column;
}
</style>
