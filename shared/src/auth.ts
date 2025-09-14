import { API } from "./client";

export async function login(username: string, password: string) {
  const response = await API.post("/auth/login/", { username, password });
  const { token } = response.data;
  localStorage.setItem("token", token);
  API.defaults.headers.common["Authorization"] = `Bearer ${token}`;
}
