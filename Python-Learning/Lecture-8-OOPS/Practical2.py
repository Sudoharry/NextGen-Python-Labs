# Create account class with 2 attributes - balance and account number
# Create methods for debit, credit & printing the balance



class Account:
    def __init__(self, bal , acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount , "is debited")
        print("Current balance is", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount , "is credited")
        print("Current balance is", self.get_balance())

    def get_balance(self):
        return self.balance  
    

acc1 = Account(10000,20222259985)
print("Balance =",acc1.balance)
print("Account Number =",acc1.account_no)
acc1.credit(1500)    
acc1.debit(1000)
acc1.credit(15000)    
acc1.credit(1500)    
acc1.debit(5000)
acc1.credit(1500)    
acc1.debit(5000)
acc1.credit(100000) 
acc1.debit(50000)