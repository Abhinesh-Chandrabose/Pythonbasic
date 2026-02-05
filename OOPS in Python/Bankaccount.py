class BankAccount:
    def __init__(self, account_number, owner_name):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = 0 # Initialized to zero as per your definition
        print(f"Bank account created for {self.owner_name} with account number {self.account_number}. Initial balance: £{self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited £{amount}. New balance: £{self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw £{amount}. New balance: £{self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")
    def get_balance(self):
        return self.balance 
# Example usage:
account1 = BankAccount("123456789", "Alice")
account1.deposit(1000)
account1.withdraw(2000)      
print(f"Current balance: £{account1.get_balance()}")


