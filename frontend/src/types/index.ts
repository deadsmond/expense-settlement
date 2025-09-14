export interface User {
    id: number;
    username: string;
    email: string;
}

export interface Expense {
    id: number;
    description: string;
    amount: number;
    date: string;
    userId: number;
}

export interface Group {
    id: number;
    name: string;
    members: User[];
}

export interface SplitExpense {
    expense: Expense;
    group: Group;
    splitAmount: number;
}