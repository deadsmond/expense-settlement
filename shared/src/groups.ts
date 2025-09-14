import { API } from "./client";
import { GroupSchema } from "./types";

export async function getGroups() {
  const res = await API.get("/groups/");
  return GroupSchema.array().parse(res.data);
}
