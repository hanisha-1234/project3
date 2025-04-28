import json
import os
from datetime import datetime

# File to store expenses
DATA_FILE = "expenses.json"

# Load existing expenses if file exists
def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

# Save expenses to the file
def save_expenses(expenses):
    with open(DATA_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

# Add a new expense
def add_expense(expenses):
    try:
        amount = float(input("Enter amount spent: ₹"))
        description = input("Enter description: ")
        category = input("Enter category (Food, Transport, Entertainment, etc.): ")
        date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
        if date == "":
            date = datetime.today().strftime('%Y-%m-%d')
        expense = {
            "amount": amount,
            "description": description,
            "category": category,
            "date": date
        }
        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added successfully!\n")
    except ValueError:
        print("Invalid input! Amount must be a number.\n")

# View all expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses to show.\n")
        return
    print("\nAll Expenses:")
    for exp in expenses:
        print(f"{exp['date']} - ₹{exp['amount']} - {exp['category']} - {exp['description']}")
    print()

# Monthly summary
def monthly_summary(expenses):
    month = input("Enter month and year (MM-YYYY): ")
    total = 0
    print(f"\nExpenses for {month}:")
    for exp in expenses:
        exp_month = datetime.strptime(exp['date'], '%Y-%m-%d').strftime('%m-%Y')
        if exp_month == month:
            print(f"{exp['date']} - ₹{exp['amount']} - {exp['category']} - {exp['description']}")
            total += exp['amount']
    print(f"Total spent in {month}: ₹{total}\n")

# Category-wise summary
def category_summary(expenses):
    category_totals = {}
    for exp in expenses:
        cat = exp['category']
        category_totals[cat] = category_totals.get(cat, 0) + exp['amount']
    
    if not category_totals:
        print("No expenses to summarize.\n")
        return
    
    print("\nCategory-wise Expenditure:")
    for cat, amount in category_totals.items():
        print(f"{cat}: ₹{amount}")
    print()

# Main menu
def main():
    expenses = load_expenses()
    while True:
        print("===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Monthly Summary")
        print("4. Category-wise Summary")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        print()
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            monthly_summary(expenses)
        elif choice == '4':
            category_summary(expenses)
        elif choice == '5':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.\n")

if __name__ == "__main__":
    main()
