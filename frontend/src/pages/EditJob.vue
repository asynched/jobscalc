<template>
  <BaseLayout pageName="Editar job">
    <div class="wrapper">
      <section class="info">
        <h1>Dados do Job</h1>
        <hr />
        <div>
          <label>
            <p>Nome do Job</p>
            <input type="text" v-model="job.name" />
          </label>
        </div>
        <div class="cols-2">
          <label>
            <p>Quantas horas<br />por dia vai dedidar ao job?</p>
            <input type="number" v-model="job.daily_hours" />
          </label>
          <label>
            <p>
              Estimativa de <br />
              horas para esse job
            </p>
            <input type="number" v-model="job.estimated_completion_time" />
          </label>
        </div>
        <div class="cols-2">
          <label>
            <p>
              Data estimada <br />
              de entrega
            </p>
            <input type="date" v-model="job.due_date" />
          </label>
          <label>
            <p>
              O projeto foi <br />
              finalizado?
            </p>
            <select v-model="job.finished">
              <option disabled selected value>Escolha uma opção</option>
              <option value="true">Sim</option>
              <option value="false">Não</option>
            </select>
          </label>
        </div>
      </section>
      <section class="total">
        <img src="@/assets/earning.png" alt="Valor" />
        <p>
          O valor do projeto ficou em <br />
          <b>R$ {{ formatValue(total) }} reais </b>
        </p>
        <div>
          <button class="save" @click="updateCurrentJob">Salvar</button>
          <button class="delete" @click="deleteCurrentJob">
            <TrashIcon />
          </button>
        </div>
      </section>
    </div>
  </BaseLayout>
</template>

<script>
  import { onBeforeMount, ref, computed } from "vue";
  import { useRoute, useRouter } from "vue-router";
  import { useToast } from "vue-toastification";
  import { TrashIcon } from "@heroicons/vue/outline";
  import {
    getJobData,
    getPlanningData,
    updateJobData,
    deleteJob,
  } from "@/helpers/requests";
  import { formatValue } from "@/helpers/format";
  import BaseLayout from "@/layouts/BaseLayout.vue";

  export default {
    name: "EditJob",
    setup() {
      const router = useRouter();
      const toast = useToast();
      const {
        params: { id },
      } = useRoute();

      const job = ref({
        id: 0,
        name: "",
        daily_hours: 0,
        estimated_completion_time: 0,
        finished: false,
        due_date: "",
        price: 0,
      });

      const planning = ref({
        expected_montly_payment: 0,
        daily_worktime: 0,
        weekly_worktime: 0,
        yearly_vacation_weeks: 0,
        hourly_value: 0,
      });

      const total = computed(
        () =>
          +job.value.estimated_completion_time * +planning.value.hourly_value
      );

      const showSuccessToast = (message) => toast.success(message);
      const showErrorToast = (message) => toast.error(message);

      const updateCurrentJob = async () => {
        try {
          await updateJobData(id, job.value);
          showSuccessToast("Dados salvos com sucesso!");
        } catch {
          showErrorToast("Erro ao salvar dados");
        }
      };

      const deleteCurrentJob = async () => {
        if (
          !window.confirm(
            "Deseja apagar esse job? Essa ação não poderá ser desfeita"
          )
        )
          return;

        try {
          await deleteJob(id);
          showSuccessToast("Job apagado com sucesso, redirecionando...");
          setTimeout(() => router.push("/dashboard"), 3000);
        } catch {
          showErrorToast("Erro ao apagar job");
        }
      };

      const fetchJob = async () => {
        const jobData = await getJobData(id);
        job.value = jobData;
      };

      const fetchPlanning = async () => {
        const planningData = await getPlanningData();
        planning.value = planningData;
      };

      onBeforeMount(async () => {
        await Promise.all([fetchJob(), fetchPlanning()]);
      });

      return {
        job,
        total,
        updateCurrentJob,
        deleteCurrentJob,
        formatValue,
      };
    },
    components: {
      BaseLayout,
      TrashIcon,
    },
  };
</script>

<style lang="scss" scoped>
  .wrapper {
    display: grid;
    grid-template-columns: 4fr 2fr;
    gap: 2rem;
  }

  .info,
  .total {
    padding: 2rem 4rem;
    margin-top: 4rem;
  }

  .info {
    section {
      margin-bottom: 4rem;
    }

    hr {
      margin: 1.5rem 0;

      border: none;
      border-top: 1px solid var(--border);
    }

    div {
      margin-bottom: 1.5rem;

      label p {
        margin-bottom: 1rem;

        font-size: 0.9rem;
      }
    }

    input,
    select {
      padding: 0.75rem 1.5rem;

      width: 100%;

      color: var(--text);

      border: 1px solid var(--border);
      border-radius: 0.25rem;

      outline: none;

      transition: var(--transition);

      &:focus,
      &:active {
        box-shadow: 0 0 0 2px rgba(0, 0, 0, 0.125);
      }
    }
  }

  .total {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    border: 1px solid var(--border);
    border-radius: 0.5rem;

    background: var(--white);

    & > * {
      margin-bottom: 2rem;
    }

    p {
      font-size: 1.125rem;
      text-align: center;
    }

    div {
      display: flex;
      gap: 1rem;

      button {
        border: none;
        border-radius: 0.5rem;

        &.save {
          padding: 0.75rem 4rem;

          color: var(--white);
          text-transform: uppercase;
          letter-spacing: 1px;

          background: var(--green);

          transition: var(--transition);

          &:hover {
            filter: brightness(1.1);
          }
        }

        &.delete {
          width: 2.5rem;
          height: 2.5rem;

          transition: var(--transition);

          svg {
            color: var(--text);
            width: 1rem;
            height: 1rem;
          }

          &:hover {
            filter: brightness(0.9);
          }
        }
      }
    }
  }

  .cols-2 {
    display: grid;
    gap: 1rem;
    grid-template-columns: repeat(2, 1fr);
  }
</style>
