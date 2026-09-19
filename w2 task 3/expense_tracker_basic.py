# Expense Tracker - Basic Level

# Create an empty list to store expenses
expenses = []


# Task 1 - Function to add expense
def add_expense():

    # Ask the user for expense name
    name = input("Enter expense name: ")

    # Ask the user for expense amount
    amount = float(input("Enter amount: "))

    # Ask the user for expense category
    category = input("Enter category: ")

    # Create a dictionary for the expense
    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    # Add the expense to the list
    expenses.append(expense)

    print("Expense added successfully!")


# Task 2 - Function to view expenses
def view_expenses():

    # Check if there are no expenses
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


# Task 3 - Function to calculate total expenses
def total_expenses():

    # Start total from zero
    total = 0

    # Add all expense amounts
    for expense in expenses:
        total = total + expense["amount"]

    # Show total expenses
    print("Total Expenses:", total)


# Task 4 - Function to search expenses by category
def search_category():

    # Ask the user for a category
    category = input("Enter category: ")

    # Assume no expense is found
    found = False

    # Check every expense
    for expense in expenses:

        # Compare categories
        if expense["category"].lower() == category.lower():

            print(
                "Name:", expense["name"],
                "Amount:", expense["amount"],
                "Category:", expense["category"]
            )

            found = True

    # If no expense is found
    if found == False:
        print("No expense found in this category.")


# Task 5 - Function to delete expense
def delete_expense():

    # Show expenses first
    view_expenses()

    # Check if there are expenses
    if len(expenses) > 0:

        # Ask for expense number
        number = int(input("Enter expense number to delete: "))

        # Check if number is valid
        if number >= 1 and number <= len(expenses):

            # Delete the selected expense
            expenses.pop(number - 1)

            print("Expense deleted successfully!")

        else:
            print("Invalid expense number.")


# Task 6 - Main Menu
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

    # Show the entered choice
    print("Choice received:", choice)

    # Choice 1
    if choice == "1":

        add_expense()

        # Pause before showing menu again
        input("Press Enter to continue...")

    # Choice 2
    elif choice == "2":

        view_expenses()

        # Pause before showing menu again
        input("Press Enter to continue...")

    # Choice 3
    elif choice == "3":

        total_expenses()

        # Pause before showing menu again
        input("Press Enter to continue...")

    # Choice 4
    elif choice == "4":

        search_category()

        # Pause before showing menu again
        input("Press Enter to continue...")

    # Choice 5
    elif choice == "5":

        delete_expense()

        # Pause before showing menu again
        input("Press Enter to continue...")

    # Choice 6
    elif choice == "6":

        print("Program ended.")
        break

    # Wrong choice
    else:

        print("Invalid choice.")

        # Pause before showing menu again
        input("Press Enter to continue...")