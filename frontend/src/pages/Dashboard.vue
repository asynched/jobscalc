<template>
  <div>
    <Header @fetchedData="handleCloseSpinner" />
    <modal-animation-wrapper>
      <spinner-modal v-if="isLoading" />
    </modal-animation-wrapper>
    <modal-animation-wrapper>
      <delete-job-modal
        v-if="showModal"
        :jobId="job"
        @close="showModal = false"
        @success="handleSuccessfullDelete"
      />
    </modal-animation-wrapper>
    <div class="wrapper">
      <job-card
        v-for="job in jobs"
        :key="job.id"
        :job="job"
        @delete="handleDeleteClick"
      />
    </div>
  </div>
</template>

<script>
import { ref, onBeforeMount } from 'vue'
import { getListOfJobs } from '@/helpers/requests'
import Header from '@/components/Header.vue'
import JobCard from '@/components/JobCard.vue'
import DeleteJobModal from '@/components/DeleteJobModal.vue'
import ModalAnimationWrapper from '@/components/ModalAnimationWrapper.vue'
import SpinnerModal from '@/components/SpinnerModal.vue'

export default {
  name: 'Dashboard',
  setup() {
    const jobs = ref([])
    const showModal = ref(false)
    const job = ref(null)
    const isLoading = ref(true)

    const fetchJobs = async () => {
      const jobsData = await getListOfJobs()
      jobs.value = jobsData
    }

    const handleCloseSpinner = () => {
      isLoading.value = false
    }

    const handleSuccessfullDelete = fetchJobs

    const handleDeleteClick = (jobId) => {
      job.value = jobId
      showModal.value = true
    }

    onBeforeMount(fetchJobs)

    return {
      job,
      jobs,
      isLoading,
      handleCloseSpinner,
      handleDeleteClick,
      handleSuccessfullDelete,
      showModal,
    }
  },

  components: {
    Header,
    JobCard,
    DeleteJobModal,
    ModalAnimationWrapper,
    SpinnerModal,
  },
}
</script>

<style lang="scss" scoped>
.wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: -4rem;
}
</style>
