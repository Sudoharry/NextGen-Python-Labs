class Engine:
    def start(self):
        print("Engine starting...")

class Car:
    def __init__(self, engine):  # engine is injected (Dependency Injection)
        self.engine = engine

    def start(self):
        self.engine.start()

engine = Engine()
car = Car(engine)
car.start()
