<template>
  <div class="card">
    <p class="id">{{ job.id }}</p>
    <h3 class="name">{{ job.name }}</h3>
    <div class="due-date">
      <p class="title">PRAZO</p>
      <p>
        <b v-if="!job.finished">{{ evaluateDate(job.due_date) }}</b>

        <b v-else>Projeto finalizado</b>
      </p>
    </div>
    <div class="price">
      <p class="title">VALOR</p>
      <p>
        <b>R$ {{ formatValue(job.price) }}</b>
      </p>
    </div>
    <button class="button in-progress" v-if="!job.finished">
      Em andamento
    </button>
    <button class="button finished" v-else>Encerrado</button>
    <div class="action">
      <router-link :to="`/edit/${job.id}`">
        <PencilAltIcon />
      </router-link>
      <button @click="handleDeleteClick">
        <TrashIcon />
      </button>
    </div>
  </div>
</template>

<script>
  import { formatValue, evaluateAndFormatDate } from "@/helpers/format.js";
  import { PencilAltIcon, TrashIcon } from "@heroicons/vue/outline";

  export default {
    name: "JobCard",
    setup({ job }, context) {
      const handleDeleteClick = () => {
        context.emit("delete", job.id);
      };

      const evaluateDate = (date) => {
        const differenceBetweenDates = evaluateAndFormatDate(date);

        if (differenceBetweenDates > 0) {
          return `${differenceBetweenDates} dias para a entrega`;
        } else if (differenceBetweenDates === 0) {
          return `Data final de entrega`;
        }

        return `O projeto está ${differenceBetweenDates * -1} dias atrasado`;
      };

      return {
        job,
        formatValue,
        handleDeleteClick,
        evaluateDate,
      };
    },
    props: ["job"],
    emits: ["delete"],
    components: {
      PencilAltIcon,
      TrashIcon,
    },
  };
</script>

<style lang="scss" scoped>
  .card {
    max-width: 70rem;
    width: 90%;

    margin: 1rem;
    padding: 1.5rem 2rem;
    background: linear-gradient(90deg, var(--white), var(--white));

    border: 1px solid var(--border);
    border-radius: 0.5rem;

    display: grid;
    align-items: center;
    justify-content: center;
    grid-template-columns: repeat(14, 1fr);
    gap: 1rem;

    transition: var(--transition);

    &:hover {
      background: linear-gradient(90deg, #fbf3ea, var(--white));

      border-left: 4px solid var(--orange);

      .id {
        color: var(--range);
      }
    }
  }

  .id {
    justify-self: center;
  }

  .name {
    grid-column: span 3;
  }

  .due-date {
    grid-column: span 3;
  }

  .price {
    grid-column: span 2;
  }

  .due-date,
  .price {
    .title {
      margin-bottom: 0.25rem;

      letter-spacing: 1px;
      color: var(--complement);
    }
  }

  .button {
    grid-column: span 3;

    padding: 0.75rem 0;

    border: none;
    border-radius: 1000px;

    &.in-progress {
      background: var(--light-green);
      color: var(--green);
    }

    &.finished {
      background: var(--light-red);
      color: var(--red);
    }

    &:hover {
      cursor: default;
    }
  }

  .action {
    grid-column: span 2;
    display: flex;
    justify-content: flex-end;
    gap: 2rem;

    button,
    a {
      display: grid;
      place-items: center;

      width: 2.5rem;
      height: 2.5rem;

      border: 1px solid var(--border);
      border-radius: 0.25rem;

      background: var(--light-grey);

      svg {
        color: var(--text);
        width: 1.25rem;
      }
    }
  }
</style>
