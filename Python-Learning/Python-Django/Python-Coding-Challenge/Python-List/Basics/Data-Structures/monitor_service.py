"""
    This script demonstrates the use of object-oriented programming (OOP) concepts in Python, 
    specifically inheritance and polymorphism. It defines a base class `Service` and two 
    derived classes `DockerService` and `JenkinsService`. Each derived class overrides the 
    `status` method to provide specific functionality.
    Classes:
        Service: A base class representing a generic service with a name and a method to 
                 check its status.
        DockerService: A subclass of `Service` that represents a Docker service and overrides 
                       the `status` method to indicate that Docker is running smoothly.
        JenkinsService: A subclass of `Service` that represents a Jenkins service and overrides 
                        the `status` method to indicate that Jenkins is running smoothly.
    Usage:
        The script creates a list of service objects (`JenkinsService` and `DockerService`) 
        and iterates through them, printing their respective statuses using polymorphism.
    
"""

class Service:
    def __init__(self, name):
        self.name = name
    
    def status(self):
        return f"Checking status of {self.name}"
    
class DockerService(Service):
    def status(self):
        return f"Docker is runnning smoothly"
    
class JenkinsService(Service):
    def status(self):
        return f"Jenkins is running smoothly"
    

services = [JenkinsService("Jenkins"), DockerService("Docker")]

for s in services:
  print(s.status())


"""
            1) Class & Object:

            - Services is a class- a blueprint for creating objects
            - It models a generic system service(like Jenkins, Docker, etc)

            2) Constructor (__init__) & self

            -  __init__ is a constructor method called when a new object is created.
            - self.name = name assigns the passed argument to the object’s instance variable.
            - self refers to the current object instance, used to access its properties.

            3) Encapsulation
            
            - The data (name) and behaviour(status) are encapsulated inside the class

            4) Inheritance

            - Both DockerService and JenkinsService inherit from the Service class.
            - This means they get all the properties and methods from Service.

            5) Method Overriding / Polymorphism

            - Each child class overrides the status() method to give custom behavior.
            - This is runtime polymorphism — the same method name (status) behaves differently depending on the class of the object.

            6) Object Instantiation & Polymorphic Behavior

            - You create instances (DockerService, JenkinsService) and store them in a list.
             - Even though you're looping over a base type (Service) reference, each call to .status() triggers the child class version (thanks to polymorphism).
      
             
                OOP Concept	          Explanation
                Class	   -->         Blueprint for services like Docker, Jenkins
                Object	   -->         Created instances like DockerService("Docker")
                Constructor-->     	    __init__ initializes object state
                Self	   -->         Refers to the current instance
                Encapsulation -->	    Data + behavior wrapped inside class
                Inheritance	  -->      DockerService & JenkinsService extend Service
                Polymorphism  -->      Overridden status() behaves differently per class

"""