"""
Define a Employee class with attribute role, department & salary. This class also has a showDetails() method.

Create an Engineer class that inherits properties from Employee &  has additional attributes: name and age
"""



class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("Role =", self.role)
        print("Dept =", self.dept)
        print("Salary =", self.salary)    
        
class Engieer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT","75000")
                
    

engg1 = Engieer("Elon Musk",40)
engg1.showDetails()        