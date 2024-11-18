class Account:
    def __init__(self, account_number, account_balance, account_type):
        self.account_number = account_number
        self.account_balance = account_balance
        self.account_type = account_type

    def deposit(self, amount):
        self.account_balance += amount
        print(f"Deposit successful! Your new balance is: {self.account_balance}")

    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient balance!")
        else:
            self.account_balance -= amount
            print(f"Withdrawal successful! Your new balance is: {self.account_balance}")

    def display(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Balance: {self.account_balance}")
        print(f"Account Type: {self.account_type}")
        print("------------------")


class SavingsAccount(Account):
    def __init__(self, account_number, account_balance, interest_rate):
        super().__init__(account_number, account_balance, "Savings")
        self.interest_rate = interest_rate

    def display(self):
        super().display()
        print(f"Interest Rate: {self.interest_rate * 100}%")
        print("------------------")


class CheckingAccount(Account):
    def __init__(self, account_number, account_balance, overdraft_limit):
        super().__init__(account_number, account_balance, "Checking")
        self.overdraft_limit = overdraft_limit

    def display(self):
        super().display()
        print(f"Overdraft Limit: {self.overdraft_limit}")
        print("------------------")


class BankSystem:
    def __init__(self):
        self.accounts = []  # List to store accounts

    def add_account(self, account):
        # Check if the account number already exists
        if any(acc.account_number == account.account_number for acc in self.accounts):
            print("\nAn account with this number already exists. Please try again.\n")
        else:
            self.accounts.append(account)
            print("\nAccount added successfully!\n")

    def remove_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                print("\nAccount removed successfully!\n")
                return
        print("\nAccount not found.\n")

    def display_accounts(self):
        print("\n")
        if not self.accounts:
            print("No accounts found.\n")
        else:
            print("Account Details:\n")
            for account in self.accounts:
                account.display()


# Menu-driven logic
def banking_menu():
    bank = BankSystem()
    while True:
        print("1. Add a Savings Account")
        print("2. Add a Checking Account")
        print("3. Remove an Account")
        print("4. Display All Accounts")
        print("5. Deposit Money")
        print("6. Withdraw Money")
        print("7. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            account_number = int(input("Enter account number: "))
            account_balance = float(input("Enter account balance: "))
            interest_rate = float(input("Enter interest rate (e.g., 0.03 for 3%): "))
            account = SavingsAccount(account_number, account_balance, interest_rate)
            bank.add_account(account)

        elif choice == 2:
            account_number = int(input("Enter account number: "))
            account_balance = float(input("Enter account balance: "))
            overdraft_limit = float(input("Enter overdraft limit: "))
            account = CheckingAccount(account_number, account_balance, overdraft_limit)
            bank.add_account(account)

        elif choice == 3:
            account_number = int(input("Enter account number to remove: "))
            bank.remove_account(account_number)

        elif choice == 4:
            bank.display_accounts()

        elif choice == 5:
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter amount to deposit: "))
            for account in bank.accounts:
                if account.account_number == account_number:
                    account.deposit(amount)
                    break
            else:
                print("Account not found.")

        elif choice == 6:
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter amount to withdraw: "))
            for account in bank.accounts:
                if account.account_number == account_number:
                    account.withdraw(amount)
                    break
            else:
                print("Account not found.")

        elif choice == 7:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

        print()


# Run the menu
banking_menu()
