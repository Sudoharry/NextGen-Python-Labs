class Student:

    # Default constructors
    def __init__ (self): 
        print("Adding the student in the Database")
        pass

    # Paramenterized constructors
    def __init__ (self, name, marks, sections):
        self.name = name
        self.marks = marks
        self.sections = sections
        print("Adding the student in the Database")


s1 = Student("Harry", 98.99, "C")
print(s1.name, s1.marks, s1.sections)

s2 = Student("Harsh", 98.00, "B")
print(s2.name, s2.marks, s2.sections)

