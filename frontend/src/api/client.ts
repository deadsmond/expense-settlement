import axios from "axios";

const API = axios.create({
  baseURL: "/api/",
  withCredentials: true,
});

export const login = async (username: string, password: string) => {
  const res = await API.post("auth/login/", { username, password });
  localStorage.setItem("token", res.data.token);
  API.defaults.headers.common["Authorization"] = `Bearer ${res.data.token}`;
};
