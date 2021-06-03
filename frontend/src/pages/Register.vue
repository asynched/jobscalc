<template>
  <div class="wrapper">
    <div class="animated">
      <h1>JobsCalc</h1>
      <p>O seu gerenciador de projetos</p>
    </div>
    <form @submit.prevent="handleSubmit">
      <h1>Cadastro</h1>
      <div class="cols-2">
        <label class="user-input">
          <p>Nome</p>
          <input type="text" v-model="user.name" />
        </label>
        <label class="user-input">
          <p>Email</p>
          <input type="email" v-model="user.email" />
        </label>
      </div>
      <label class="user-input">
        <p>Senha</p>
        <input type="password" v-model="user.password" />
      </label>
      <button>Cadastrar</button>
    </form>
  </div>
</template>

<script>
  import { reactive } from "vue";
  import { useToast } from "vue-toastification";
  import { useRouter } from "vue-router";
  import { registerUser } from "../helpers/requests";

  export default {
    name: "Register",

    setup() {
      const toast = useToast();
      const router = useRouter();

      const user = reactive({
        name: "",
        email: "",
        password: "",
      });

      const handleSubmit = async () => {
        try {
          const { name, email, password } = user;

          await registerUser(name, email, password);
          toast.success("Cadastrado com sucesso, redirecionando...");

          setTimeout(() => {
            router.push({ path: "/" });
          }, 2000);
        } catch {
          toast.error(
            "Erro ao cadastrar\nVerifique os dados e tente novamente."
          );
        }
      };

      return {
        user,
        handleSubmit,
      };
    },
  };
</script>

<style lang="scss" scoped>
  .wrapper {
    width: 100vw;
    height: 100vh;

    display: grid;
    grid-template-columns: 4fr 5fr;
    place-items: center;

    background: var(--light-grey);
  }

  form {
    max-width: 48rem;
    width: 90%;

    padding: 4rem;

    background: var(--white);

    border: 1px solid var(--border);
    border-radius: 0.5rem;
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
</style>
