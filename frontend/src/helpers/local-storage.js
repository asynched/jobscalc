export const saveTokenToLocalStorage = (token) =>
  localStorage.setItem("_token", token);

export const getTokenFromLocalStorage = () => localStorage.getItem("_token");

export const clearTokenFromLocalStorage = () =>
  localStorage.removeItem("_token");
