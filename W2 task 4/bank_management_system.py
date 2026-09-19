# TASK 4 - Bank Account Management System

# Create BankAccount class
class BankAccount:

    # Initialize account details
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    # Deposit money
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Money deposited successfully.")

    # Withdraw money
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Money withdrawn successfully.")
        else:
            print("Insufficient balance.")

    # Check balance
    def check_balance(self):
        print("Current Balance:", self.balance)

    # Display account information
    def display_info(self):
        print("Account Holder:", self.name)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


# Create account
name = input("Enter account holder name: ")
account_number = input("Enter account number: ")
balance = float(input("Enter initial balance: "))

account = BankAccount(name, account_number, balance)


# Menu
while True:

    print("\n1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Display Account Information")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
        input("Press Enter to continue...")

    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
        input("Press Enter to continue...")

    elif choice == "3":
        account.check_balance()
        input("Press Enter to continue...")

    elif choice == "4":
        account.display_info()
        input("Press Enter to continue...")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")
        input("Press Enter to continue...")