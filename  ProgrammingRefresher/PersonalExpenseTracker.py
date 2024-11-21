import csv
from datetime import datetime

expenses = []
monthly_budget = 0

def add_expense():
    date = input("Enter the date of the expense (YYYY-MM-DD): ")
    category = input("Enter the category of the expense (e.g., Food, Travel): ")
    amount = float(input("Enter the amount spent: "))
    description = input("Enter a brief description of the expense: ")
    
    expense = {
        'date': date,
        'category': category,
        'amount': amount,
        'description': description
    }
    
    expenses.append(expense)
    print("Expense added successfully!")

def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return
    
    for expense in expenses:
        if all(key in expense for key in ('date', 'category', 'amount', 'description')):
            print(f"Date: {expense['date']}, Category: {expense['category']}, Amount: {expense['amount']}, Description: {expense['description']}")
        else:
            print("Incomplete expense entry found, skipping...")

def set_budget():
    global monthly_budget
    monthly_budget = float(input("Enter your monthly budget: "))
    print(f"Monthly budget set to {monthly_budget}")

def track_budget():
    total_expenses = sum(expense['amount'] for expense in expenses)
    if total_expenses > monthly_budget:
        print("You have exceeded your budget!")
    else:
        print(f"You have {monthly_budget - total_expenses} left for the month")

def save_expenses():
    with open('expenses.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['date', 'category', 'amount', 'description'])
        writer.writeheader()
        writer.writerows(expenses)
    print("Expenses saved to expenses.csv")

def load_expenses():
    try:
        with open('expenses.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append(row)
        print("Expenses loaded from expenses.csv")
    except FileNotFoundError:
        print("No previous expenses found.")

def display_menu():
    while True:
        print("\nMenu:")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Track budget")
        print("4. Save expenses")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            set_budget()
            track_budget()
        elif choice == '4':
            save_expenses()
        elif choice == '5':
            save_expenses()
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    load_expenses()
    display_menu()