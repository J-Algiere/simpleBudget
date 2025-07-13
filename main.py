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
    # Create a new budget with $0 starting balance
    my_budget = Budget(starting_balance=0)

    #creating a CLI for user to update/view budget

    while True:
        print("\n----- Monthly Budget -----\n")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show History")
        print("4. Show Balance")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            try:
                my_budget.add_transaction(Income(input("Add description: "), float(input("Add income amount: "))))
            except ValueError:
                print()
                print("Please enter a valid number. (450.50)")
        elif choice == "2":
            try:
                my_budget.add_transaction(Expense(input("Add description: "), float(input("Add expense amount: ")),input("Add category: ")))
            except ValueError:
                print()
                print("Please enter a valid number. (50.75)")
        elif choice == "3":
            my_budget.show_history()
        elif choice == "4":
            print(f"\nCurrent Balance: {my_budget.balance:.2f}")
        elif choice == "5":
            print("\nExiting...")
            break
        else:
            print("\nInvalid choice, please try again\n")



if __name__ == "__main__":
    main()
