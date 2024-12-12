# Custom Exception for Invalid Inputs
class InvalidInputException(Exception):
    pass

# Abstract Base Class (Demonstrates Abstraction)
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_number, account_balance, name, phone, email):
        if account_number <= 0:
            raise InvalidInputException("Account number must be positive.")
        if account_balance < 0:
            raise InvalidInputException("Account balance cannot be negative.")
        self.__account_number = account_number
        self.__account_balance = account_balance
        self.__name = name
        self.__phone = phone
        self.__email = email

    @property
    def account_number(self):
        return self.__account_number

    @property
    def account_balance(self):
        return self.__account_balance

    @account_balance.setter
    def account_balance(self, value):
        if value < 0:
            raise InvalidInputException("Account balance cannot be negative.")
        self.__account_balance = value

    @property
    def name(self):
        return self.__name

    @property
    def phone(self):
        return self.__phone

    @property
    def email(self):
        return self.__email

    def display_personal_info(self):
        print(f"Name: {self.__name}")
        print(f"Phone: {self.__phone}")
        print(f"Email: {self.__email}")

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def display(self):
        pass


class SavingsAccount(Account):
    def __init__(self, account_number, account_balance, name, phone, email, interest_rate):
        super().__init__(account_number, account_balance, name, phone, email)
        if interest_rate < 0:
            raise InvalidInputException("Interest rate cannot be negative.")
        self.__interest_rate = interest_rate

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidInputException("Deposit amount must be positive.")
        self.account_balance += amount
        print(f"Deposit successful! New balance: {self.account_balance}")

    def withdraw(self, amount):
        if amount <= 0 or amount > self.account_balance:
            raise InvalidInputException("Invalid withdrawal amount.")
        self.account_balance -= amount
        print(f"Withdrawal successful! New balance: {self.account_balance}")

    def display(self):
        print(f"Savings Account Number: {self.account_number}")
        print(f"Balance: {self.account_balance}")
        print(f"Interest Rate: {self.__interest_rate * 100}%")
        self.display_personal_info()
        print()


class LoanAccount(Account):
    def __init__(self, account_number, account_balance, name, phone, email, loan_amount, interest_rate):
        super().__init__(account_number, account_balance, name, phone, email)
        if loan_amount < 0:
            raise InvalidInputException("Loan amount cannot be negative.")
        if interest_rate < 0:
            raise InvalidInputException("Interest rate cannot be negative.")
        self.__loan_amount = loan_amount
        self.__interest_rate = interest_rate

    def deposit(self, amount):
        """Represents payment towards the loan balance."""
        if amount <= 0:
            raise InvalidInputException("Payment amount must be positive.")
        self.__loan_amount -= amount
        print(f"Payment successful! Remaining loan balance: {self.__loan_amount}")

    def withdraw(self, amount):
        """Loan accounts don't support withdrawal."""
        raise InvalidInputException("Withdrawals are not allowed in loan accounts.")

    def borrow_loan(self, amount):
        if amount <= 0:
            raise InvalidInputException("Loan amount must be positive.")
        self.__loan_amount += amount
        print(f"Loan approved! New loan balance: {self.__loan_amount}")

    def pay_loan(self, amount):
        if amount <= 0 or amount > self.__loan_amount:
            raise InvalidInputException("Invalid loan payment amount.")
        self.__loan_amount -= amount
        print(f"Loan payment successful! Remaining loan balance: {self.__loan_amount}")

    def display(self):
        print(f"Loan Account Number: {self.account_number}")
        print(f"Balance: {self.account_balance}")
        print(f"Loan Amount: {self.__loan_amount}")
        print(f"Loan Interest Rate: {self.__interest_rate * 100}%")
        self.display_personal_info()
        print()


class BankSystem:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        if any(acc.account_number == account.account_number for acc in self.accounts):
            raise InvalidInputException("Account number already exists.")
        self.accounts.append(account)
        print("Account added successfully!")

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def remove_account(self, account_number):
        account = self.find_account(account_number)
        if account is None:
            raise InvalidInputException("Account not found.")
        self.accounts.remove(account)
        print(f"Account {account_number} removed successfully!")

    def display_accounts(self, admin_mode=False, current_user=None):
        if not self.accounts:
            print("No accounts found.")
        else:
            for account in self.accounts:
                if admin_mode or (current_user and current_user.account_number == account.account_number):
                    account.display()

def banking_menu():
    bank = BankSystem()
    current_user = None
    admin_mode = False

    while True:
        try:
            print("\nLogin Options:")
            print("1. Admin Login")
            print("2. User Login")
            print("3. Exit")
            login_choice = int(input("Enter your choice: "))

            if login_choice == 1:
                password = input("Enter admin password: ")
                if password == "1742":
                    admin_mode = True
                    print("Admin login successful!")
                else:
                    print("Invalid admin password!")
                    continue

            elif login_choice == 2:
                try:
                    account_number = int(input("Enter your account number: "))
                except ValueError:
                    print("Invalid account number! Please enter a number.")
                    continue

                current_user = bank.find_account(account_number)

                if current_user is None:
                    print("Account number seems new. Would you like to create a new account?")
                    create_choice = input("Enter 'yes' to create a new account, or 'no' to cancel: ").lower()

                    if create_choice == 'yes':
                        name = input("Enter your name: ")
                        phone = input("Enter your phone number: ")
                        email = input("Enter your email: ")
                        balance = float(input("Enter opening balance: "))
                        print("1. Savings Account")
                        print("2. Loan Account")
                        acc_type = int(input("Enter account type: "))

                        if acc_type == 1:
                            interest_rate = float(input("Enter interest rate (e.g., 0.05 for 5%): "))
                            new_account = SavingsAccount(account_number, balance, name, phone, email, interest_rate)
                        elif acc_type == 2:
                            loan_amount = float(input("Enter loan amount: "))
                            interest_rate = float(input("Enter loan interest rate (e.g., 0.05 for 5%): "))
                            new_account = LoanAccount(account_number, balance, name, phone, email, loan_amount, interest_rate)
                        else:
                            print("Invalid account type.")
                            continue

                        bank.add_account(new_account)
                        current_user = new_account
                    else:
                        print("Returning to login menu.")
                        continue

                print("User login successful!")

            elif login_choice == 3:
                print("Exiting...")
                break

            else:
                print("Invalid choice! Please try again.")
                continue

            # Banking options loop
            while True:
                print("\nBanking Options:")
                if admin_mode:
                    # Admin options: Add, Remove, Display Accounts
                    print("1. Add Account")
                    print("2. Remove Account")
                    print("3. Display All Accounts")
                else:
                    # User options: View personal account, Deposit, Withdraw, Loan repayment, Bill payment
                    print("4. View Personal Account")
                    print("5. Deposit")
                    print("6. Withdraw")
                    print("7. Repay Loan")
                    print("8. Pay Bill")
                print("9. Logout")

                try:
                    choice = int(input("Enter your choice: "))

                    if admin_mode and choice == 1:
                        acc_no = int(input("Enter Account Number: "))
                        name = input("Enter Name: ")
                        phone = input("Enter Phone Number: ")
                        email = input("Enter Email: ")
                        balance = float(input("Enter Balance: "))
                        interest_rate = float(input("Enter Interest Rate (e.g., 0.05 for 5%): "))
                        account = SavingsAccount(acc_no, balance, name, phone, email, interest_rate)
                        bank.add_account(account)

                    elif admin_mode and choice == 2:
                        acc_no = int(input("Enter Account Number to Remove: "))
                        bank.remove_account(acc_no)

                    elif admin_mode and choice == 3:
                        print("All accounts:")
                        bank.display_accounts(admin_mode=True)

                    elif not admin_mode and choice == 4:
                        if current_user:
                            current_user.display()
                        else:
                            print("No account logged in.")

                    elif not admin_mode and choice == 5:
                        if current_user:
                            amount = float(input("Enter Deposit Amount: "))
                            current_user.deposit(amount)
                        else:
                            print("No account logged in.")

                    elif not admin_mode and choice == 6:
                        if current_user:
                            amount = float(input("Enter Withdrawal Amount: "))
                            current_user.withdraw(amount)
                        else:
                            print("No account logged in.")

                    elif not admin_mode and choice == 7:
                        if isinstance(current_user, LoanAccount):
                            amount = float(input("Enter Loan Repayment Amount: "))
                            current_user.pay_loan(amount)
                        else:
                            print("Loan repayment is only available for loan accounts.")

                    elif not admin_mode and choice == 8:
                        if current_user:
                            print("\nBill Payment Options:")
                            print("1. Electricity Bill")
                            print("2. Internet Bill")
                            print("3. Tution Fee")
                            print("4. Other")

                            bill_choice = int(input("Enter your choice: "))
                            if bill_choice == 1:
                                bill_type = "Electricity"
                            elif bill_choice == 2:
                                bill_type = "Internet"
                            elif bill_choice == 3:
                                bill_type = "Tution"
                            elif bill_choice == 4:
                                bill_type = input("Enter bill type: ")
                            else:
                                print("Invalid choice!")
                                continue

                            bill_account = input(f"Enter {bill_type} Account/ID: ")
                            amount = float(input(f"Enter {bill_type} Bill Amount: "))
                            if amount <= 0 or amount > current_user.account_balance:
                                print("Invalid bill payment amount.")
                                continue

                            current_user.withdraw(amount)
                            print(f"{bill_type} bill paid successfully!")
                        else:
                            print("No account logged in.")

                    elif choice == 9:
                        print("Logging out...")
                        admin_mode = False
                        current_user = None
                        break

                    else:
                        print("Invalid choice! Please try again.")

                except InvalidInputException as e:
                    print(f"Error: {e}")
                except ValueError:
                    print("Invalid input! Please enter valid numbers.")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")

        except InvalidInputException as e:
            print(f"Error: {e}")
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Run the menu
banking_menu()
