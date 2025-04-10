""" 
    Build a Car class with properties and methods like start() and stop().
"""

class Car:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
        self.running = False
    
    def start(self):
        if not self.running:
            self.running = True
            print(f'{self.brand} {self.model} started.')
        else:
            print(f'{self.brand} {self.model} is already running')
    
    def stop(self):
        if self.running:
            self.running = False
            print(f'{self.brand} {self.model} stopped')
        else:
            print(f'{self.brand} {self.model} is already stopped')


car = Car('Toyota', 'Camry')
car.stop()