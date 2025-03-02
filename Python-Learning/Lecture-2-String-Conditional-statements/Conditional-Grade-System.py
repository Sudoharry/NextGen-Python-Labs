# Calculate the Grades based on the marks

marks = int(input("Enter your marks for grade calculation:"))

if (marks >= 90):
    grade = "A"

elif (marks >= 80 and marks < 90):
    grade = "B"

elif (marks >= 70 and marks < 80):
    grade = "C"

elif (marks < 70 and marks < 70):
    grade = "D"   


print ("Grade of the student is:", grade)    