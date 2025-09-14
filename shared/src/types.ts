import { z } from "zod";

export const UserSchema = z.object({
  id: z.number(),
  username: z.string(),
});

export const GroupSchema = z.object({
  id: z.number(),
  name: z.string(),
});

export const ExpenseSchema = z.object({
  id: z.number(),
  amount: z.number(),
  description: z.string().optional(),
  paid_by: z.number(),
  group: z.number(),
  created_at: z.string(),
});

export type User = z.infer<typeof UserSchema>;
export type Group = z.infer<typeof GroupSchema>;
export type Expense = z.infer<typeof ExpenseSchema>;
