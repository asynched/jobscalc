<template>
  <BaseLayout pageName="Meu perfil">
    <modal-animation-wrapper>
      <spinner-modal v-if="isLoading" />
    </modal-animation-wrapper>
    <div class="wrapper">
      <!-- Perfil -->
      <div class="profile">
        <img :src="profile.image_url" :alt="profile.name" />
        <h1>{{ profile.name }}</h1>
        <p>
          O valor da sua hora é de <br />
          <b>R$ ${{ formatValue(hourly_value) }} reais</b>
        </p>
        <button @click="handleSubmit">Salvar dados</button>
        <button @click="handleLogoff" class="logoff">Sair</button>
      </div>
      <!-- Dados -->
      <div class="info">
        <section>
          <h1>Dados do perfil</h1>
          <hr />
          <div class="cols-2">
            <input type="text" placeholder="Nome" v-model="profile.name" />
            <input
              type="text"
              placeholder="Link da foto"
              v-model="profile.image_url"
            />
          </div>
        </section>
        <section>
          <h1>Planejamento</h1>
          <hr />
          <div class="cols-2">
            <label>
              <p>
                Quanto eu<br />
                quero ganhar por mês?
              </p>
              <input
                type="number"
                placeholder="R$"
                v-model="planning.expected_montly_payment"
              />
            </label>
            <label>
              <p>
                Quantas horas<br />
                quero trabalhar por dia
              </p>
              <input
                type="number"
                placeholder="6 horas..."
                v-model="planning.daily_worktime"
              />
            </label>
          </div>
          <div class="cols-2">
            <label>
              <p>
                Quantos dias quero<br />
                trabalhar por semana?
              </p>
              <input
                type="number"
                placeholder="5 dias..."
                v-model="planning.weekly_worktime"
              />
            </label>
            <label>
              <p>
                Quantas semanas<br />
                por ano você quer tirar férias?
              </p>
              <input
                type="number"
                placeholder="4 semanas..."
                v-model="planning.yearly_vacation_weeks"
              />
            </label>
          </div>
        </section>
      </div>
    </div>
  </BaseLayout>
</template>

<script>
import { ref, computed, onBeforeMount } from 'vue'
import {
  getProfileData,
  getPlanningData,
  updateProfileData,
  updatePlanningData,
} from '@/helpers/requests'
import { formatValue } from '@/helpers/format'
import { calculateHourlyValue } from '@/helpers/calculate'
import BaseLayout from '@/layouts/BaseLayout.vue'
import { useToast } from 'vue-toastification'
import { useRouter } from 'vue-router'
import { clearTokenFromLocalStorage } from '../helpers/local-storage'
import ModalAnimationWrapper from '@/components/ModalAnimationWrapper.vue'
import SpinnerModal from '@/components/SpinnerModal.vue'

export default {
  name: 'Profile',
  setup() {
    const router = useRouter()
    const toast = useToast()

    const isLoading = ref(true)

    const profile = ref({
      name: '',
      image_url: '',
    })

    const planning = ref({
      expected_montly_payment: 0,
      daily_worktime: 0,
      weekly_worktime: 0,
      yearly_vacation_weeks: 0,
      hourly_value: 0,
    })

    const showSuccessToast = () =>
      toast.success('Dados atualizados com sucesso!')
    const showErrorToast = () => toast.error('Erro ao atualizar dados')

    const handleSubmit = async () => {
      try {
        await Promise.all([
          updateProfileData(profile.value),
          updatePlanningData(planning.value),
        ])
        showSuccessToast()
      } catch {
        showErrorToast()
      }
    }

    const handleLogoff = () => {
      clearTokenFromLocalStorage()
      router.push({ path: '/' })
    }

    const hourly_value = computed(() =>
      calculateHourlyValue(
        +planning.value.expected_montly_payment,
        +planning.value.daily_worktime,
        +planning.value.weekly_worktime,
        +planning.value.yearly_vacation_weeks
      )
    )

    onBeforeMount(async () => {
      const [profileData, planningData] = await Promise.all([
        getProfileData(),
        getPlanningData(),
      ])

      profile.value = profileData
      planning.value = planningData
      isLoading.value = false
    })

    return {
      isLoading,
      handleLogoff,
      handleSubmit,
      formatValue,
      planning,
      hourly_value,
      profile,
    }
  },
  components: {
    BaseLayout,
    ModalAnimationWrapper,
    SpinnerModal,
  },
}
</script>

<style lang="scss" scoped>
.wrapper {
  width: 100%;
  height: calc(100vh - 4rem);

  display: grid;
  grid-template-columns: 2fr 4fr;
  gap: 4rem;
}

.info,
.profile {
  margin: 4rem 0;

  display: flex;
  flex-direction: column;
  justify-content: center;

  background: var(--white);

  border: 1px solid var(--border);
  border-radius: 0.5rem;
}

.profile {
  align-items: center;

  & > * {
    margin: 1rem 0;
  }

  img {
    height: 12rem;
    width: 12rem;

    object-fit: cover;
    background: var(--purple);

    border: 2px solid var(--orange);
    border-radius: 50%;
  }

  p {
    font-size: 1.125rem;
    text-align: center;
  }

  button {
    padding: 0.75rem 0;

    width: 14rem;

    letter-spacing: 1px;
    font-weight: 600;
    text-transform: uppercase;
    color: var(--white);

    border: none;
    border-radius: 0.5rem;

    background: var(--green);

    transition: var(--transition);

    &:hover {
      filter: brightness(1.1);
    }

    &.logoff {
      background: var(--red);
    }
  }
}

.info {
  padding: 4rem;

  section {
    margin-bottom: 2rem;
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

  input {
    padding: 0.75rem 1.5rem;

    width: 100%;

    color: var(--text);

    border: 1px solid var(--border);
    border-radius: 0.25rem;

    outline: none;

    transition: var(--transition);

    &:focus,
    &:active {
      box-shadow: 0 0 0 2px rgba(54, 178, 54, 1);
    }
  }
}

.cols-2 {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(2, 1fr);
}
</style>
