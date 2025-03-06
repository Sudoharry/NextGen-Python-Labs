class Person:
    name = "anonymous"  #.. class attribute


    def changeName(self, name): #..
        self.__class__.name = "Harry"  #.. Change self into Person and new object won't be created here./ 
        #self.__class__

    @classmethod  #.. decorator 
    def changeName(cls, name):
        cls.name = name
            



p1 = Person()
p1.changeName("Harry")
print(p1.name)  #.. When we create a variable of person and call the changeName then it will call "Harry" which I passed here as argument.
print(Person.name)   #.. When we call the class name(Person), it will call anonymous as name here