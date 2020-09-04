<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <p @click="goHome()" class="navbar-brand h-100 m-0 p-0 home" href="#">
        Stock News
      </p>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item">
            <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
          </li>
        </ul>
      </div>
    </nav>
  </div>
</template>

<script>
  export default {
    methods: {
      goHome() {
        this.$router.push('/')
      }
    }
  }
</script>

<style lang="scss" scoped>
  .home {
    cursor: pointer;
  }
</style>