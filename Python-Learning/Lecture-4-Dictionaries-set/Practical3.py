## WAP to enter the marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. 
## Use subjects name as key and marks as value.

marks = {}

subject1 = int(input("Enter the Maths marks:"))
marks.update({"Maths": subject1})

subject2 = int(input("Enter the Science marks:"))
marks.update({"Science": subject2})

subject3 = int(input("Enter the Computer marks:"))
marks.update({"Computer": subject3})

print(marks)


## Solution: We can take the inputs from the user and store the key value pair in the dictionary using the marks.update({"Maths": subject1 (variables user input)})
