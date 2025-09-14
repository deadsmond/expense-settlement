import axios from "axios";

const token = localStorage.getItem("token");
export const API = axios.create({
  baseURL: "/api/",
  headers: token ? { Authorization: `Bearer ${token}` } : {},
});
