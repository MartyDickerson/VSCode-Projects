import csv
import os

FILE = "expenses.csv"

def add_expense(amount, category):
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([amount, category])
    print("✅ Expense added.")

def show_expenses():
    if not os.path.exists(FILE):
        print("No expenses recorded yet.")
        return
    total = 0
    with open(FILE, "r") as f:
        reader = csv.reader(f)
        print("\n--- Expenses ---")
        for row in reader:
            amount, category = row
            print(f"${amount} - {category}")
            total += float(amount)
    print(f"\n💰 Total Spent: ${total:.2f}")

if __name__ == "__main__":
    while True:
        print("\nOptions: [a]dd expense, [v]iew expenses, [q]uit")
        choice = input("Choose: ").lower()
        if choice == "a":
            amount = float(input("Amount: "))
            category = input("Category: ")
            add_expense(amount, category)
        elif choice == "v":
            show_expenses()
        elif choice == "q":
            break
        else:
            print("Invalid option.")
