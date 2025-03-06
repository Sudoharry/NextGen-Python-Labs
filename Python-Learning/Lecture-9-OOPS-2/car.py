class Car:      # Parent method through which the toyotaCar and Fortuner class has inherited the attributes and methods
    # color = "Black"
    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stopped..")


class ToyotaCar(Car):  #.. Car class was inherited to ToyataCar derived/child method
    def __init__(self, brand):
        self.name = brand


class Fortuner(ToyotaCar):  ##. Multi-level inheritance
    def __init__(self,type):
        self.type = type


car1= Fortuner("Diesel")
car1.start()               

# car1 = ToyotaCar("Fortuner")
# car2 = ToyotaCar("Camry")    
# # print(car1.start())    
# print(car1.color)
# print(car2.color)
# # print(car2.name)                
# # car1.start()
# # car1.stop()