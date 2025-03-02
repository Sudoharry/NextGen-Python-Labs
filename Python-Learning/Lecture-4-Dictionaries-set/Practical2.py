## You are given a list of subjects for students.Assume one classroom is required for 1 subject. How many classrooms are required for all the subjects.

subjects = {
    "python","java","C++","python","javascript"
    "java","python","java","C++","C"
}

print(subjects.union())
print(type(subjects))
print(len(subjects.union()))




# Solution: We can use the set as it will only store the unique subjects, and we can count how many numbers of classes would be required and then use the len 
## to count the number of classes in the number.