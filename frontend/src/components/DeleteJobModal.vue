<template>
  <Modal>
    <div class="content">
      <TrashIcon />
      <h1>Excluir job</h1>
      <p>
        Quer mesmo excluir esse job? <br />
        Ele será apagado para sempre.
      </p>
      <div>
        <button class="cancel" @click="closeModal">Cancelar</button>
        <button class="delete" @click="handleDeleteClick">Excluir</button>
      </div>
    </div>
  </Modal>
</template>

<script>
import Modal from '@/components/Modal.vue'
import { TrashIcon } from '@heroicons/vue/outline'
import { useToast } from 'vue-toastification'
import { deleteJob } from '@/helpers/requests'

export default {
  name: 'DeleteJobModal',
  setup(props, context) {
    const toast = useToast()

    const showSuccessToast = () => toast.success('Job apagado com sucesso!')
    const showErrorToast = () => toast.error('Erro ao apagar job!')

    const closeModal = () => context.emit('close')

    const handleDeleteClick = async () => {
      try {
        await deleteJob(props.jobId)
        showSuccessToast()
        closeModal()
        context.emit('success')
      } catch {
        showErrorToast()
      }
    }

    return {
      props,
      closeModal,
      handleDeleteClick,
    }
  },
  props: ['jobId'],
  emits: ['close', 'success'],
  components: {
    Modal,
    TrashIcon,
  },
}
</script>

<style lang="scss" scoped>
div.content {
  padding: 2rem;

  max-width: 30rem;
  width: 90%;

  text-align: center;

  background: var(--white);

  border-radius: 0.5rem;

  box-shadow: 0 0 2rem rgba(32, 32, 32, 0.125);

  h1,
  svg,
  p {
    margin-bottom: 1.5rem;
  }

  svg {
    width: 5rem;
  }

  div {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
    margin-top: 2.5rem;

    button {
      padding: 1rem;

      border: none;
      border-radius: 0.5rem;

      letter-spacing: 1px;
      text-transform: uppercase;

      &.cancel {
        color: var(--text);
        background: var(--grey);
      }

      &.delete {
        color: var(--white);
        background: var(--red);
      }
    }
  }
}
</style>
