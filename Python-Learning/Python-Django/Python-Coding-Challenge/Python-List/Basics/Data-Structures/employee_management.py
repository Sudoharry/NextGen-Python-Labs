# Basics OOPs example - Employee Management

class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    
    def show_details(self):
        return f"{self.name} works as a {self.role}"

emp1 = Employee("Harendra Barot","Python Devops Engineer")
print(emp1.show_details())

# 🧠 Concepts: Class, Object, Constructor, Instance Variable, Method
