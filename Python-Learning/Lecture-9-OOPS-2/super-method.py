class Car:      # Parent method through which the toyotaCar and Fortuner class has inherited the attributes and methods
    def __init__(self, type):  ## constructor added here
        self.type = type

    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stopped..")


class ToyotaCar(Car):  #.. Car class was inherited to ToyataCar derived/child method
    def __init__(self, name, type):
        super().__init__(type)  #.. Keep it start so that the parent class properties get set first.
        self.name = name
        super().start() #.. Parent class object call can be done by super() method, we can access it.
        



car1 = ToyotaCar("Camry","Electric")
print(car1.type)