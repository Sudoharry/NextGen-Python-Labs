class Engine:
    def start(self):
        print("Engine starting...")

class Car:
    def __init__(self):
        self.engine = Engine()  # tightly coupled to Engine class

    def start(self):
        self.engine.start()
        
engine = Engine()
car = Car(engine)
car.start()