"""
    Dictionary(dict): A dict is unordered collection of key value pairs
"""

# Syntax & Examples

student = {'name': 'Harry', 'age': 29, 'course': 'Python'}
# print(student['course'])

student['age'] = 30
student['city'] = 'Gandhidham'
student['country'] = 'India'
student['phone'] = 8849964295

print(student)

# Looping through a dict
print('Students Record:')
for key, value in student.items():
    print(key, ':', value)