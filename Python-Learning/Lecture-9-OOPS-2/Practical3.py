"""
Create a class called Order which stores items & its price.
  Use Dunder function __gt__() to convey that:
     order1 > order2 if price of order1 > price of order2 

"""


class Order:
    def __init__(self, items, price):
        self.items = items
        self.price = price

    def __gt__(self,order2):   #.. __gt__ is here and we don't see any errors. If used without it'll throw error. "> not supported in the instance type object"
        return self.price > order2.price    

order1 = Order("Chips", 250)
order2 = Order("Tea", 50)     
 
print(order1 > order2) 