<template>
  <div>
    <header>
      <div>
        <p @click="router.go(-1)" class="go-back"><ArrowLeftIcon /></p>
        <p>{{ pageName }}</p>
        <p>&nbsp;</p>
      </div>
    </header>
    <main class="base-layout-wrapper">
      <div class="base-layout-wrapper">
        <slot></slot>
      </div>
    </main>
  </div>
</template>

<script>
import { onBeforeMount } from 'vue'
import { ArrowLeftIcon } from '@heroicons/vue/outline'
import { useRouter } from 'vue-router'
import { setPageTitle } from '@/helpers/utils'

export default {
  name: 'BaseLayout',
  setup(props) {
    const router = useRouter()

    onBeforeMount(() => setPageTitle(props.pageName))

    return {
      router,
      ...props,
    }
  },
  props: ['pageName'],
  components: {
    ArrowLeftIcon,
  },
}
</script>

<style lang="scss" scoped>
header {
  display: flex;
  align-items: center;
  justify-content: center;

  height: 4rem;

  background: var(--purple);

  div {
    padding: 1rem 0;

    max-width: 70rem;
    width: 90%;

    display: flex;
    justify-content: space-between;

    color: var(--complement);

    p.go-back:hover {
      cursor: pointer;
    }

    svg {
      width: 1rem;
    }
  }
}

main.base-layout-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
}

div.base-layout-wrapper {
  max-width: 70rem;
  width: 90%;
}
</style>
