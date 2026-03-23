import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt

expenses = []
BUDGET = 0

# ------------------ Load Expenses ------------------
def load_expenses():
    if os.path.exists("expenses.csv"):
        with open("expenses.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append({
                    "date": row["Date"],
                    "name": row["Name"],
                    "category": row["Category"],
                    "amount": float(row["Amount"])
                })

# ------------------ Save Expenses ------------------
def save_expenses():
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Name", "Category", "Amount"])
        for exp in expenses:
            writer.writerow([exp["date"], exp["name"], exp["category"], exp["amount"]])

# ------------------ Add Expense ------------------
def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food/Travel/Shopping/Others): ")
    date = datetime.now().strftime("%Y-%m-%d")

    expenses.append({
        "date": date,
        "name": name,
        "category": category,
        "amount": amount
    })

    print("Expense added successfully!")

# ------------------ View Expenses ------------------
def show_expenses():
    if not expenses:
        print("No expenses found")
        return

    print("\nAll Expenses:")
    for i, exp in enumerate(expenses):
        print(f"{i+1}. {exp['date']} | {exp['name']} | {exp['category']} | ₹{exp['amount']}")

# ------------------ Total Expense ------------------
def total_expense():
    total = sum(exp["amount"] for exp in expenses)
    print("Total Expense: ₹", total)

    if BUDGET > 0 and total > BUDGET:
        print("⚠ Warning: Budget Exceeded!")

# ------------------ Delete Expense ------------------
def delete_expense():
    show_expenses()
    num = int(input("Enter expense number to delete: "))
    if 0 < num <= len(expenses):
        expenses.pop(num - 1)
        print("Expense deleted")
    else:
        print("Invalid number")

# ------------------ Search Expense ------------------
def search_expense():
    keyword = input("Enter expense name to search: ").lower()
    found = False
    for exp in expenses:
        if keyword in exp["name"].lower():
            print(exp["date"], exp["name"], exp["category"], exp["amount"])
            found = True
    if not found:
        print("No matching expense found")

# ------------------ Set Budget ------------------
def set_budget():
    global BUDGET
    BUDGET = float(input("Enter monthly budget: "))
    print("Budget set successfully")

# ------------------ Show Pie Chart ------------------
def show_chart():
    if not expenses:
        print("No data to show")
        return

    categories = {}
    for exp in expenses:
        cat = exp["category"]
        categories[cat] = categories.get(cat, 0) + exp["amount"]

    plt.pie(categories.values(), labels=categories.keys(), autopct='%1.1f%%')
    plt.title("Expense Distribution")
    plt.show()

# ------------------ Main Menu ------------------
load_expenses()

while True:
    print("\n====== Expense Tracker ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Delete Expense")
    print("5. Search Expense")
    print("6. Set Budget")
    print("7. Show Chart")
    print("8. Save & Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        delete_expense()
    elif choice == "5":
        search_expense()
    elif choice == "6":
        set_budget()
    elif choice == "7":
        show_chart()
    elif choice == "8":
        save_expenses()
        print("Expenses saved. Goodbye!")
        break
    else:
        print("Invalid choice")
