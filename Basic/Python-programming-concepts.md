## 1)Variables and Data Types

- Variables: Used to store data
     
      Ex:
        name = "Harry"     # String
        age = 28           # Integer
        height = 6.2       # Float 
        is_student = True  # Boolean

- Data Types
  
      - int: Whole number (e.g., 1, -10)
      - float: Decimal numbers (e.g., 3.14)
      - str: Text (e.g., "hello")
      - bool: True or False


## 2) Input and Output

- Input: Accept user input.
        
       Ex: name = input ("Enter your name: ")

- Output: Print data to the console.
     
       Ex: print(f"Hello, {name}")
 
## 3) Conditional Statements:

- Used for decision-making:
      
  - If-else: 
        
       ex: 

          age = int (input("Enter your age: "))
          if age >= 18:
              print("You are an adult.")
          else:
              print("You are a minor.")  
    
  - Elif (Else if):
          
           ex:
              score = 75
              if score >= 90:
                 print("Grade: A")
              elif score >= 80:
                 print("Grade: B")
              else:
                 print("Grade: C")
## 4. Loops
Used to repeat actions.

- For Loop: Iterates over a sequence.


       for i in range(5):
          print(i)  # Prints 0 to 4

 - While Loop: Runs until a condition is false.

         count = 0
         while count < 5:
            print(count)
            count += 1

## 5. Functions
   
Reusable blocks of code.

 -  Defining and Calling:

        def greet(name):
           return f"Hello, {name}!"

    print(greet("Harry"))


## 6. Data Structures

   - Lists: Ordered collection.


      fruits = ["apple", "banana", "papaya"]
      print(fruits[0])  # Access element
      fruits.append("orange")  # Add element

  - Dictionaries: Key-value pairs.

      person = {"name": "Harry", "age": 28}
      print(person["name"])

  - Tuples: Immutable ordered collection.

      coordinates = (10, 20)
      print(coordinates[0])

  - Sets: Unordered collection of unique elements.


       numbers = {1, 2, 3, 3}
       print(numbers)  # {1, 2, 3}

## 7. Error Handling
    Used to handle exceptions.

    try:
        num = int(input("Enter a number: "))
        print(10 / num)
    except ValueError:
        print("Invalid input! Please enter a number.")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    finally:
        print("Execution complete.")

## 8. File Handling

   - Read File:

     with open("example.txt", "r") as file:
     content = file.read()
     print(content)

   - Write to File:

       with open("example.txt", "w") as file:
       file.write("Hello, World!")
     
## 9. Classes and Objects (OOP Basics)
     - Defining a Class:
        class Person:
           def __init__(self, name, age):
             self.name = name
             self.age = age

        def greet(self):
           return f"Hi, I'm {self.name}."

        alice = Person("Harry", 28)
        print(alice.greet())

## 10. Modules and Libraries
       - Importing Modules:

           import math 
           print(math.sqrt(16))
    
      - Using Libraries:

           import random
           print(random.randint(1, 10))
