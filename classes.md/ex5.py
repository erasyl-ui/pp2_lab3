"""""""
5. Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. 
   - Withdrawals may not exceed the available balance. 
   - Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
"""""""

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount}. New Balance: {self.balance}")

# Example:
# acct = Account("John Doe", 500)
# acct.deposit(200) → New balance: 700
# acct.withdraw(100) → New balance: 600
# acct.withdraw(700) → Cannot withdraw (insufficient balance)

acct = Account("John Doe", 500)
acct.deposit(200)
acct.withdraw(100)
acct.withdraw(700)
