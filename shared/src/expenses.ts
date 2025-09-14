import { API } from "./client";
import { ExpenseSchema } from "./types";

export async function createExpense(data: {
  group: number;
  amount: number;
  paid_by: number;
  description?: string;
}) {
  const res = await API.post("/expenses/", data);
  return ExpenseSchema.parse(res.data);
}

export async function getExpenses(groupId: number) {
  const res = await API.get(`/expenses/?group=${groupId}`);
  return ExpenseSchema.array().parse(res.data);
}
