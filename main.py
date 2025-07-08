from abc import ABC, abstractmethod

class Budget:

    def __init__(self, starting_balance=0):
        self.balance = starting_balance
        self.transactions = []

    def add_income(self, description, amount):
        self.balance += amount
        self.transactions.append({'type': 'Income', 'description': description, 'amount': amount})


    def add_expense(self, category, description, amount):
        self.balance -= amount
        self.transactions.append({'type': 'Expense', 'category': category, 'description': description, 'amount': amount})

    def show_balance(self):
        return self.balance

    def show_history(self):
        for entry in self.transactions:
            if entry['type'] == 'Income':
                print(f'Income: {entry["description"]} | Amount: ${entry["amount"]}')
            elif entry['type'] == 'Expense':
                print(f"Expense: {entry['description']} | Category: {entry: 'category} | Amount: -${entry['amount']}")



def main():
    ...


if __name__ == "__main__":
    main()
