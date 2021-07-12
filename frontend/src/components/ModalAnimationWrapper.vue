<template>
  <transition name="display" mode="in-out" appear>
    <slot />
  </transition>
</template>

<script>
export default {
  name: 'ModalAnimationWrapper',
}
</script>

<style lang="scss" scoped>
.display-enter-active,
.display-leave-active {
  transition: opacity 0.5s ease;
}

.display-enter-from,
.display-leave-to {
  opacity: 0;
}
</style>
