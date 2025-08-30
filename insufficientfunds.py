# Define the custom exception
class InsufficientFunds(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__("Insufficient funds: Cannot withdraw the requested amount with the current balance.")

# Define a BankAccount class
class BankAccount:
    def __init__(self, account_number, account_holder_name, balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited", amount, "rupees. New balance:", self.balance, "rupees.")

    def withdraw(self, amount):
        try:
            if self.balance - amount < 1000:
                raise InsufficientFunds(self.balance, amount)
            self.balance -= amount
            print("Withdrew", amount, "rupees. New balance:", self.balance, "rupees.")
        except InsufficientFunds as e:
            print(e)

    def display_account_info(self):
        print("Account Number:", self.account_number)
        print("Account Holder Name:", self.account_holder_name)
        print("Account Balance:", self.balance, "rupees")


account = BankAccount("123456789", "Johnny Deep", 1500)
account.display_account_info()
account.deposit(500)
#account.withdraw(500)
account.withdraw(2000) 
