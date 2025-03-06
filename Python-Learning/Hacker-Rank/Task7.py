"""
The first line contains the integer n, the number of students' records. The next n lines contain the names and marks obtained by a student, each value separated by a space. 
The final line contains query_name, the name of a student to query.

"""


if __name__ == '__main__':
    n = int(input())  #. Number of students record
    student_marks = {}
    
    for _ in range(n):
        name, *line = input().split() #.. Read input and split into a list
        scores = list(map(float, line))  
        student_marks[name] = scores
    
    query_name = input()
    avg_marks = sum(student_marks[query_name]) / 3 #.. Calculate average
    print(f"{avg_marks:.2f}") #.. Print the average with 2 decimal value.


"""
Read input n → Number of students.
Read n lines → Each contains a student’s name followed by three space-separated marks.
Store data in a dictionary → The student’s name is the key, and the marks (as a list of floats) are the values.
Read the query name → Get the student's marks from the dictionary.
Compute the average → Use sum(marks) / 3.
Print the result → Format to two decimal places using f"{value:.2f}".

"""