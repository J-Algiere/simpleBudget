from abc import ABC, abstractmethod

class Transaction(ABC):
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount

    @abstractmethod
    def apply(self, budget):
        pass

class Income(Transaction):
    def apply(self, budget):
        budget.balance += self.amount
        budget.transactions.append(self)

class Expense(Transaction):
    def __init__(self, description, amount, category):
        super().__init__(description, amount)
        self.category = category

    def apply(self, budget):
        budget.balance -= self.amount
        budget.transactions.append(self)

class Budget:
    def __init__(self, starting_balance=0):
        self.balance = starting_balance
        self.transactions = []

    def add_transaction(self, transaction):
        transaction.apply(self)

    def show_history(self):
        print("\n--- Transaction History ---")
        for entry in self.transactions:
            if isinstance(entry, Income):
                print(f"[Income]  {entry.description:<15} +${entry.amount:.2f}")
            elif isinstance(entry, Expense):
                print(f"[Expense] {entry.description:<15} -${entry.amount:.2f}   (Category: {entry.category})")
        print("---------------------------")
        print(f"Current Balance: ${self.balance:.2f}\n")



def main():
    # Create a new budget with $1000 starting balance
    my_budget = Budget(starting_balance=1000)

    # Add income and expenses
    my_budget.add_transaction(Income("Paycheck", 1500))
    my_budget.add_transaction(Expense("Groceries", 200, "Food"))
    my_budget.add_transaction(Expense("Gas", 60, "Transportation"))
    my_budget.add_transaction(Income("Freelance", 400))
    my_budget.add_transaction(Expense("Rent", 1000, "Housing"))
    my_budget.add_transaction(Income("VA", 2300))

    # Show transaction history and final balance
    my_budget.show_history()



if __name__ == "__main__":
    main()
