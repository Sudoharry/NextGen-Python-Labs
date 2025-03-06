class Student:   # class defined this way
    college_name = "Charusat"  ## class attibutes

    def __init__(self, name, marks):    # Initialized the parameterized constructor always in the class first (It's used to initialized the object)
        self.name = name    # name object   (object attributes)
        self.marks = marks  # marks object

    def welcome(self):   #.. methods
        print("Welcome students,", self.name)    # Welcome students

    def get_marks(self):   # get marks 
        return self.marks
    

s1 = Student("Harry", 98)  # object is created this way
s1.welcome()
print(s1.get_marks())    