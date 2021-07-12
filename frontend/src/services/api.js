import axios from 'axios'
import { getTokenFromLocalStorage } from '../helpers/local-storage'

const makeAuthorizationHeaders = (token = getTokenFromLocalStorage()) => {
  if (token) {
    return {
      Authorization: `Bearer ${token}`,
    }
  }

  return {}
}

const API = axios.create({
  baseURL: 'http://localhost:8000/api/',
  headers: {
    ...makeAuthorizationHeaders(),
  },
})

export const setAuthorizationheaders = (token = getTokenFromLocalStorage()) => {
  API.defaults.headers['Authorization'] = `Bearer ${token}`
}

export default API
