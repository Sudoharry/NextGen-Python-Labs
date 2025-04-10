
""" 
    Make a BankAccount class with deposit and withdraw methods.
"""
class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self,amount):
        self.balance += amount
        print(f'Deposited ${amount}. New balance: $ {self.balance}')


    def withdrawal(self,amount):
        if amount > self.balance:
            print('Insufficient funds')
        else:
            self.balance -= amount
            print(f'Withdrawal ${amount}. Remaining balance: ${self.balance}')

# Example
account = BankAccount('Bob', 1000)
account.deposit(500)
account.withdrawal(700)
