<template>
  <div>
    <Header />
    <ModalAnimationWrapper>
      <DeleteJobModal
        v-if="showModal"
        :jobId="job"
        @close="showModal = false"
        @success="handleSuccessfullDelete"
      />
    </ModalAnimationWrapper>
    <div class="wrapper">
      <JobCard
        v-for="job in jobs"
        :key="job.id"
        :job="job"
        @delete="handleDeleteClick"
      />
    </div>
  </div>
</template>

<script>
  import { ref, onBeforeMount } from "vue";
  import { getListOfJobs } from "@/helpers/requests";
  import Header from "@/components/Header.vue";
  import JobCard from "@/components/JobCard.vue";
  import DeleteJobModal from "@/components/DeleteJobModal.vue";
  import ModalAnimationWrapper from "@/components/ModalAnimationWrapper.vue";

  export default {
    name: "Dashboard",
    setup() {
      const jobs = ref([]);
      const showModal = ref(false);
      const job = ref(null);

      const fetchJobs = async () => {
        const jobsData = await getListOfJobs();
        jobs.value = jobsData;
      };

      const handleSuccessfullDelete = fetchJobs;

      const handleDeleteClick = (jobId) => {
        job.value = jobId;
        showModal.value = true;
      };

      onBeforeMount(fetchJobs);

      return {
        job,
        jobs,
        handleDeleteClick,
        handleSuccessfullDelete,
        showModal,
      };
    },

    components: {
      Header,
      JobCard,
      DeleteJobModal,
      ModalAnimationWrapper,
    },
  };
</script>

<style lang="scss" scoped>
  .wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: -4rem;
  }
</style>
