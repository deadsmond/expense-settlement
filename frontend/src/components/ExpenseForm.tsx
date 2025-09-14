import React, { useEffect, useState } from 'react';
import { Expense } from '../types';
import { fetchExpenses } from '../api/client.ts';

const ExpenseList: React.FC = () => {
    const [expenses, setExpenses] = useState<Expense[]>([]);
    const [loading, setLoading] = useState<boolean>(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const loadExpenses = async () => {
            try {
                const data = await fetchExpenses();
                setExpenses(data);
            } catch (err) {
                setError('Failed to load expenses');
            } finally {
                setLoading(false);
            }
        };

        loadExpenses();
    }, []);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>{error}</div>;
    }

    return (
        <div>
            <h2>Expense List</h2>
            <ul>
                {expenses.map(expense => (
                    <li key={expense.id}>
                        {expense.description}: ${expense.amount}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ExpenseList;