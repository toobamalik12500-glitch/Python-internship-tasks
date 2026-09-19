# Expense Tracker - Intermediate Level

import json


# Create an empty list to store expenses
expenses = []


# Task 1 - Save expenses to file
def save_expenses():

    # Open the file in write mode
    with open("expenses.json", "w") as file:

        # Save expenses in JSON file
        json.dump(expenses, file, indent=4)


# Task 2 - Load expenses from file
def load_expenses():

    global expenses

    try:

        # Open the file in read mode
        with open("expenses.json", "r") as file:

            # Read expenses from file
            expenses = json.load(file)

    except FileNotFoundError:

        # If file does not exist, keep list empty
        expenses = []


# Task 3 - Function to add expense
def add_expense():

    # Ask for expense name
    name = input("Enter expense name: ")

    # Ask for expense amount
    amount = float(input("Enter amount: "))

    # Ask for expense category
    category = input("Enter category: ")

    # Create expense dictionary
    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    # Add expense to list
    expenses.append(expense)

    # Save updated expenses
    save_expenses()

    # Show success message
    print("Expense added successfully!")


# Task 4 - Function to view expenses
def view_expenses():

    # Check if list is empty
    if len(expenses) == 0:

        print("No expenses found.")

    else:

        # Show all expenses
        for i in range(len(expenses)):

            print(
                "Expense", i + 1,
                "Name:", expenses[i]["name"],
                "Amount:", expenses[i]["amount"],
                "Category:", expenses[i]["category"]
            )


# Task 5 - Function to calculate total expenses
def total_expenses():

    # Start total from zero
    total = 0

    # Add all expense amounts
    for expense in expenses:

        total = total + expense["amount"]

    # Show total
    print("Total Expenses:", total)


# Task 6 - Function to search by category
def search_category():

    # Ask for category
    category = input("Enter category: ")

    # Assume no expense is found
    found = False

    # Check each expense
    for expense in expenses:

        # Compare category
        if expense["category"].lower() == category.lower():

            print(
                "Name:", expense["name"],
                "Amount:", expense["amount"],
                "Category:", expense["category"]
            )

            found = True

    # If no matching expense is found
    if found == False:

        print("No expense found in this category.")


# Task 7 - Function to delete expense
def delete_expense():

    # Show all expenses
    view_expenses()

    # Check if expenses exist
    if len(expenses) > 0:

        # Ask which expense to delete
        number = int(input("Enter expense number to delete: "))

        # Check if number is valid
        if number >= 1 and number <= len(expenses):

            # Delete selected expense
            expenses.pop(number - 1)

            # Save updated expenses
            save_expenses()

            print("Expense deleted successfully!")

        else:

            print("Invalid expense number.")


# Load saved expenses when program starts
load_expenses()


# Task 8 - Main Menu
while True:

    print()
    print("===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Search by Category")
    print("5. Delete Expense")
    print("6. Exit")

    # Ask user for choice
    choice = input("Enter your choice: ")

    # Show entered choice
    print("Choice received:", choice)

    # Choice 1
    if choice == "1":

        add_expense()

        input("Press Enter to continue...")

    # Choice 2
    elif choice == "2":

        view_expenses()

        input("Press Enter to continue...")

    # Choice 3
    elif choice == "3":

        total_expenses()

        input("Press Enter to continue...")

    # Choice 4
    elif choice == "4":

        search_category()

        input("Press Enter to continue...")

    # Choice 5
    elif choice == "5":

        delete_expense()

        input("Press Enter to continue...")

    # Choice 6
    elif choice == "6":

        print("Program ended.")
        break

    # Invalid choice
    else:

        print("Invalid choice.")

        input("Press Enter to continue...")