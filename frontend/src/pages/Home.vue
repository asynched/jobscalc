<template>
  <div class="wrapper">
    <form @submit.prevent="handleSubmit">
      <div class="logo">
        <img src="@/assets/favicon.png" alt="JobsCalc" />
        <h1>JobsCalc</h1>
      </div>
      <label class="user-input">
        <p>Email</p>
        <input type="email" v-model="user.email" />
      </label>
      <label class="user-input">
        <p>Senha</p>
        <input type="password" v-model="user.password" />
      </label>
      <button>Login</button>
      <div class="options">
        <label>
          <input type="checkbox" />
          <span>Lembrar-me</span>
        </label>
        <router-link to="/register">Registrar-me</router-link>
      </div>
    </form>
    <div class="animated">
      <h1>JobsCalc</h1>
      <p>O seu gerenciador de projetos</p>
    </div>
  </div>
</template>

<script>
  import { reactive } from "vue";
  import { getAuthorizationToken } from "@/helpers/requests";
  import { saveTokenToLocalStorage } from "@/helpers/local-storage";
  import { setAuthorizationheaders } from "@/services/api";
  import { useToast } from "vue-toastification";
  import { useRouter } from "vue-router";

  export default {
    name: "Home",
    setup() {
      const router = useRouter();
      const toast = useToast();

      const user = reactive({
        email: "",
        password: "",
      });

      const handleSubmit = async () => {
        const { email, password } = user;

        try {
          const { access } = await getAuthorizationToken(email, password);
          saveTokenToLocalStorage(access);
          setAuthorizationheaders(access);
          router.push({ path: "/dashboard" });
        } catch {
          toast.error("Credenciais incorretas!");
        }
      };

      return {
        handleSubmit,
        user,
      };
    },
    components: {},
  };
</script>

<style lang="scss" scoped>
  .wrapper {
    width: 100vw;
    height: 100vh;

    display: grid;
    grid-template-columns: repeat(2, 1fr);
    place-items: center;
  }

  form {
    max-width: 32rem;
    width: 90%;

    padding: 4rem;

    div.logo {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 1rem;
    }

    label.user-input {
      display: flex;
      flex-direction: column;

      margin: 2rem 0;

      p {
        margin-bottom: 1rem;
        font-size: 1.25rem;
      }

      input {
        width: 100%;
        padding: 0.75rem 1rem;

        border: 1px solid var(--border);
        border-radius: 0.25rem;

        outline: none;

        color: var(--text);

        transition: var(--transition);

        &:active,
        &:focus {
          box-shadow: 0 0 0 2px rgba(32, 32, 32, 0.125);
        }
      }
    }

    button {
      margin-bottom: 1.5rem;
      padding: 1rem 0;

      width: 100%;

      border: none;
      border-radius: 0.25rem;

      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 2px;
      color: var(--white);

      background: var(--green);

      transition: var(--transition);

      &:hover {
        filter: brightness(1.1);
      }
    }

    div.options {
      display: flex;
      justify-content: space-between;
      align-items: center;

      label {
        display: flex;
        align-items: center;
        gap: 0.5rem;
      }
    }
  }

  div.animated {
    width: 100%;
    height: 100%;

    background: var(--purple);

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    color: var(--white);

    animation: hue-rotate 2s infinite;

    h1 {
      font-size: 3rem;
      animation: title-animation 1s;
    }

    p {
      font-size: 1.25rem;
      animation: title-animation 1s;
      animation-delay: 250ms;
      animation-fill-mode: backwards;
    }
  }

  @keyframes title-animation {
    from {
      opacity: 0;
      transform: translate(-50%, 0);
    }
    to {
      opacity: 1;
      transform: translate(0, 0);
    }
  }

  @keyframes hue-rotate {
    from {
      filter: hue-rotate(0);
    }
    50% {
      filter: hue-rotate(45deg);
    }
    to {
      filter: hue-rotate(0);
    }
  }
</style>
