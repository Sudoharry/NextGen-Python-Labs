
class Car:
    def __init__(self):
        self.acc = False    #.. unnecessary steps that is not been visible to a user if they try to start the car
        self.brk = False
        self.clutch = False

    def start(self):      #.. unncessary things not traceble
        self.acc = True
        self.clutch = True
        print("Car Engine start...")

car1 = Car()  
car1.start()    #.. Necessary things that are in control of the user.


# This concepts is called as abstraction in the OOPS.

