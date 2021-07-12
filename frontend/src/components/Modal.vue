<template>
  <transition name="display" mode="out-in">
    <div class="modal-content-wrapper">
      <slot />
    </div>
  </transition>
</template>

<script>
export default {
  name: 'Modal',
}
</script>

<style lang="scss" scoped>
div.modal-content-wrapper {
  width: 100vw;
  height: 100vh;

  position: fixed;
  top: 0;
  left: 0;
  z-index: 10;

  display: grid;
  place-items: center;

  background: rgba(65, 65, 76, 0.75);
  backdrop-filter: blur(4px);
}
</style>
