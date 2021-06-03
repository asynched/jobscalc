<template>
  <header>
    <!-- Upper part -->
    <div class="upper">
      <!-- Logo -->
      <img src="@/assets/logo.png" alt="JobsCalc" />
      <!-- Profile info -->
      <div class="profile-info">
        <div>
          <p>
            <b>{{ profile.name }}</b>
          </p>
          <router-link to="/profile">Ver perfil</router-link>
        </div>
        <img :src="profile.image_url" :alt="profile.name" />
      </div>
    </div>

    <div class="lower">
      <!-- Projetos -->
      <div class="project-info">
        <div>
          <h2>{{ projects.total }}</h2>
          <p>Projetos ao total</p>
        </div>
        <div>
          <h2>{{ projects.in_progress }}</h2>
          <p>Em andamento</p>
        </div>
        <div>
          <h2>{{ projects.finished }}</h2>
          <p>Encerrados</p>
        </div>
      </div>
      <router-link to="/create">
        <div><PlusIcon /></div>
        <span>Adicionar novo job</span>
      </router-link>
    </div>
  </header>
</template>

<script>
  import { ref, onBeforeMount } from "vue";
  import { PlusIcon } from "@heroicons/vue/outline";
  import { getProfileData, getJobsInfo } from "@/helpers/requests";

  export default {
    name: "Header",

    setup() {
      const profile = ref({
        name: "",
        image_url: "",
      });

      const projects = ref({
        total: 0,
        in_progress: 0,
        finished: 0,
      });

      onBeforeMount(async () => {
        const [profileData, projectsData] = await Promise.all([
          getProfileData(),
          getJobsInfo(),
        ]);

        profile.value = profileData;
        projects.value = projectsData;
      });

      return {
        profile,
        projects,
      };
    },
    components: {
      PlusIcon,
    },
  };
</script>

<style lang="scss" scoped>
  header {
    display: flex;
    flex-direction: column;
    align-items: center;

    color: var(--white);
    background: var(--purple);

    .upper,
    .lower {
      max-width: 70rem;
      width: 90%;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .upper {
      padding: 1rem 0;

      .profile-info {
        display: flex;
        gap: 1rem;
        align-items: center;

        a {
          font-size: 0.9rem;
          color: var(--complement);

          &:hover {
            color: var(--orange);
          }
        }

        b {
          font-size: 1.25rem;
        }

        img {
          width: 4rem;
          height: 4rem;

          object-fit: cover;

          border: 2px solid var(--orange);
          border-radius: 50%;
        }
      }
    }

    .lower {
      padding: 0.5rem 0 5rem 0;

      & > div {
        display: flex;
        align-items: center;
        gap: 2rem;

        & p {
          color: var(--complement);
        }
      }

      a {
        text-decoration: none;
        padding: 0.75rem 1rem;

        display: flex;
        align-items: center;
        gap: 1rem;

        border: none;
        border-radius: 0.5rem;

        color: var(--white);

        background: var(--orange);

        transition: var(--transition);

        div {
          width: 2rem;
          height: 2rem;

          background: rgba(255, 255, 255, 0.15);
          display: grid;

          place-items: center;

          border-radius: 0.25rem;

          svg {
            width: 1rem;
          }
        }

        span {
          font-weight: 600;
          letter-spacing: 1px;
          text-transform: uppercase;
        }

        &:hover {
          filter: brightness(1.1);
        }
      }
    }
  }
</style>
