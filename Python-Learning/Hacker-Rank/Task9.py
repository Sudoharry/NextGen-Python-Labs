"""
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example

records=[["chi","20.0"],["beta","50.0"],["alpha","50.0"]]

The ordered list of scores is [20.0,50.0] , so the second lowest score is 50.0 . There are two students with that score:["beta","alpha"] . Ordered alphabetically, the names are printed as:

"""

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score]) #.. Append name and score as pair
        
        
    # Get unique scores and find the second lowest
    unique_scores = sorted(set(score for name, score in students))    
    second_lowest = unique_scores[1]
     
     
    # Get names of students with the second lowest score
    names = sorted([name for name, score in students if score == second_lowest])
     
     
    # Print each name as new line
    for name in names:
     print(name)
     

"""
Explanation:
 Read the number of students.
 Store the names and grades in a list (students).
 Extract unique scores and sort them to find the second lowest.
 Retrieve students with the second lowest score and sort their names alphabetically.
 Print each name on a new line.
"""