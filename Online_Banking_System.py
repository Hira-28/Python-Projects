from abc import ABC, abstractmethod


class BankException(Exception):
    """Custom exception for bank-related errors."""
    def __init__(self, message):
        super().__init__(message)


# Abstract Base Class (Demonstrates Abstraction)
class Account(ABC):
    def __init__(self, account_number, account_balance):
        self.__account_number = account_number
        self.__account_balance = account_balance

    # Encapsulation with property
    @property
    def account_number(self):
        return self.__account_number

    @property
    def account_balance(self):
        return self.__account_balance

    @account_balance.setter
    def account_balance(self, value):
        if value < 0:
            raise BankException("Balance cannot be negative!")
        self.__account_balance = value

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def display(self):
        pass


# Single Inheritance
class SavingsAccount(Account):
    def __init__(self, account_number, account_balance, interest_rate):
        super().__init__(account_number, account_balance)
        self.__interest_rate = interest_rate

    def deposit(self, amount):
        if amount <= 0:
            raise BankException("Deposit amount must be greater than zero!")
        self.account_balance += amount
        print(f"Deposit successful! New balance: {self.account_balance}")

    def withdraw(self, amount):
        if amount > self.account_balance:
            raise BankException("Insufficient balance!")
        self.account_balance -= amount
        print(f"Withdrawal successful! New balance: {self.account_balance}")

    def display(self):
        print(f"Savings Account Number: {self.account_number}")
        print(f"Balance: {self.account_balance}")
        print(f"Interest Rate: {self.__interest_rate * 100}%\n")


# Multilevel Inheritance
class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, account_number, account_balance, interest_rate, loyalty_bonus):
        super().__init__(account_number, account_balance, interest_rate)
        self.__loyalty_bonus = loyalty_bonus

    def add_loyalty_bonus(self):
        self.account_balance += self.__loyalty_bonus
        print(f"Loyalty bonus of {self.__loyalty_bonus} added! New balance: {self.account_balance}")

    def display(self):
        super().display()
        print(f"Loyalty Bonus: {self.__loyalty_bonus}\n")


# Hierarchical Inheritance
class BusinessAccount(Account):
    def __init__(self, account_number, account_balance, overdraft_limit):
        super().__init__(account_number, account_balance)
        self.__overdraft_limit = overdraft_limit

    def deposit(self, amount):
        if amount <= 0:
            raise BankException("Deposit amount must be greater than zero!")
        self.account_balance += amount
        print(f"Deposit successful! New balance: {self.account_balance}")

    def withdraw(self, amount):
        if amount > self.account_balance + self.__overdraft_limit:
            raise BankException("Overdraft limit exceeded!")
        self.account_balance -= amount
        print(f"Withdrawal successful! New balance: {self.account_balance}")

    def display(self):
        print(f"Business Account Number: {self.account_number}")
        print(f"Balance: {self.account_balance}")
        print(f"Overdraft Limit: {self.__overdraft_limit}\n")


# Hybrid Inheritance
class LoanAccount(Account):
    def __init__(self, account_number, account_balance, loan_amount, interest_rate):
        super().__init__(account_number, account_balance)
        self.__loan_amount = loan_amount
        self.__interest_rate = interest_rate
        self.__repaid_amount = 0

    def repay(self, amount):
        if amount > self.__loan_amount - self.__repaid_amount:
            raise BankException("Cannot repay more than the outstanding loan!")
        self.__repaid_amount += amount
        self.account_balance -= amount
        print(f"Repayment successful! Remaining loan: {self.__loan_amount - self.__repaid_amount}")

    def deposit(self, amount):
        raise BankException("Deposits are not allowed in loan accounts!")

    def withdraw(self, amount):
        raise BankException("Withdrawals are not allowed in loan accounts!")

    def display(self):
        print(f"Loan Account Number: {self.account_number}")
        print(f"Balance: {self.account_balance}")
        print(f"Loan Amount: {self.__loan_amount}")
        print(f"Interest Rate: {self.__interest_rate * 100}%")
        print(f"Repaid Amount: {self.__repaid_amount}\n")


# Bank System for Managing Accounts
class BankSystem:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        if any(acc.account_number == account.account_number for acc in self.accounts):
            raise BankException("An account with this number already exists!")
        self.accounts.append(account)
        print("Account added successfully!")

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        raise BankException("Account not found!")

    def display_accounts(self):
        if not self.accounts:
            print("No accounts found.")
        else:
            for account in self.accounts:
                account.display()


# Menu System
def banking_menu():
    bank = BankSystem()
    while True:
        try:
            print("\n1. Add Savings Account")
            print("2. Add Premium Savings Account")
            print("3. Add Business Account")
            print("4. Add Loan Account")
            print("5. Display Accounts")
            print("6. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                acc_no = int(input("Enter Account Number: "))
                balance = float(input("Enter Balance: "))
                interest_rate = float(input("Enter Interest Rate (e.g., 0.05 for 5%): "))
                account = SavingsAccount(acc_no, balance, interest_rate)
                bank.add_account(account)

            elif choice == 2:
                acc_no = int(input("Enter Account Number: "))
                balance = float(input("Enter Balance: "))
                interest_rate = float(input("Enter Interest Rate (e.g., 0.05 for 5%): "))
                loyalty_bonus = float(input("Enter Loyalty Bonus: "))
                account = PremiumSavingsAccount(acc_no, balance, interest_rate, loyalty_bonus)
                bank.add_account(account)

            elif choice == 3:
                acc_no = int(input("Enter Account Number: "))
                balance = float(input("Enter Balance: "))
                overdraft = float(input("Enter Overdraft Limit: "))
                account = BusinessAccount(acc_no, balance, overdraft)
                bank.add_account(account)

            elif choice == 4:
                acc_no = int(input("Enter Account Number: "))
                balance = float(input("Enter Balance: "))
                loan_amount = float(input("Enter Loan Amount: "))
                interest_rate = float(input("Enter Interest Rate (e.g., 0.1 for 10%): "))
                account = LoanAccount(acc_no, balance, loan_amount, interest_rate)
                bank.add_account(account)

            elif choice == 5:
                bank.display_accounts()

            elif choice == 6:
                print("Exiting...")
                break

            else:
                print("Invalid choice!")

        except BankException as e:
            print(f"Error: {e}")
        except ValueError:
            print("Invalid input! Please enter a number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


# Run the menu
banking_menu()
