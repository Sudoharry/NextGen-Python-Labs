"""
     What is coupling ?

     Coupling refers to the degree of dependency between different modules, classes or components in a system

     Think of it like:

        "How tightly are these two pieces of codes connected to each other"

"""


"""  
     Types of Coupling :

     1) Tight Coupling(Bad):

     - When two modules/classes are heavily dependendent on each other
     - A change in one can likely break or affect the other
     - Hard to test, reuse and maintain

     Ex: 
     class Engine:
        def start(self):
            print("Engine starting...")

    class Car:
        def __init__(self):
            self.engine = Engine()  # tightly coupled to Engine class

        def start(self):
            self.engine.start()

    
     Note: Here, Car is hardcoded to use the Engine class. If Engine changes, Car might break.


     2) Loose Coupling (Good):

     - When modules interacts via interfacesor abstractions, not direct implementation
     - Easier to update, test and use 


     Ex: Improved Version:

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

"""