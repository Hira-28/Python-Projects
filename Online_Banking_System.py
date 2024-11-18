class Account:
    def __init__(self, account_number, account_balance, account_type):
        self.account_number = account_number
        self.account_balance = account_balance
        self.account_type = account_type

    def details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Balance: {self.account_balance}")
        print(f"Account Type: {self.account_type}")

    def deposit(self):
        da = float(input("Enter your Deposit Amount: "))
        new_balance = self.account_balance + da
        print("Deposit Successful!")
        print(f"Your previous Account Balance was: {self.account_balance}")
        print(f"After Deposit, your New Account Balance is: {new_balance}")
        self.account_balance = new_balance

    def withdraw(self):
        wa = float(input("Enter your Withdraw Amount: "))
        if wa > self.account_balance:
            print("Insufficient Balance!")
        else:
            new_balance = self.account_balance - wa
            print("Withdraw Successful!")
            print(f"Your previous Account Balance was: {self.account_balance}")
            print(f"After Withdraw, your New Account Balance is: {new_balance}")
            self.account_balance = new_balance


class SavingsAccount(Account):
    def __init__(self, account_number, account_balance, account_type, interest_rate):
        super().__init__(account_number, account_balance, account_type)
        self.interest_rate = interest_rate

    def details(self):
        super().details()
        sb = self.account_balance + (self.account_balance * self.interest_rate)
        print(f"Saving Account Balance (with interest): {sb}")


class CheckingAccount(Account):
    def __init__(self, account_number, account_balance, account_type, ca_balance):
        super().__init__(account_number, account_balance, account_type)
        self.ca_balance = ca_balance

    def display(self):
        super().details()
        print(f"Checking Account Number: {self.account_number}")
        print(f"Checking Account Balance: {self.ca_balance}")


class Customer:
    def __init__(self, customer_id, name, address, account):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.account = account

    def display(self):
        print(f"Customer Name: {self.name}")
        print(f"Customer ID: {self.customer_id}")
        print(f"Customer Address: {self.address}")
        print()
        self.account.details()


# Main Function
def main():
    account = Account(1742, 500000, "Savings")
    customer = Customer(1730, "Mehedi", "Ashuliya", account)
    savings_account = SavingsAccount(1730, 500000, "Savings", 0.03)
    checking_account = CheckingAccount(1671, 500000, "Savings", 20000)

    customer.display()
    account.deposit()
    account.withdraw()
    print()
    savings_account.details()
    print()
    checking_account.display()


# Calling the main function
main()
