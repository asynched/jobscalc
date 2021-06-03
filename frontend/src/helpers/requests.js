import API from "@/services/api";

export const getProfileData = async () => {
  const { data } = await API.get("profile/");

  return data;
};

export const updateProfileData = async (profile) => {
  await API.put("profile/", profile);
};

export const getJobsInfo = async () => {
  const { data } = await API.get("jobs/data/");

  return data;
};

export const getListOfJobs = async () => {
  const { data } = await API.get("jobs/");

  return data;
};

export const getJobData = async (id) => {
  const { data } = await API.get(`jobs/${id}/`);

  return data;
};

export const createJob = async (jobData) => {
  const { data } = await API.post("jobs/", jobData);

  return data;
};

export const updateJobData = async (id, data) => {
  await API.put(`jobs/${id}/`, data);
};

export const deleteJob = async (jobId) => {
  await API.delete(`jobs/${jobId}/`);
};

export const getPlanningData = async () => {
  const { data } = await API.get("planning/");

  return data;
};

export const updatePlanningData = async (planning) => {
  await API.put("planning/", planning);
};

export const getAuthorizationToken = async (email, password) => {
  const { data } = await API.post("token/", {
    email,
    password,
  });

  return data;
};

export const registerUser = async (name, email, password) => {
  await API.post("register/", {
    name,
    email,
    password,
  });
};
