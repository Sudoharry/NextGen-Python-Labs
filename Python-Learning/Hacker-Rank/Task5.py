"""
Print the list of integers from  i through n  as a string, without spaces.

"""

if __name__ == '__main__':
    n = int(input("Enter number from 1 to 9:"))
    print(*range(1, n + 1), sep='')



"""
 Reading Input: n = int(input()) reads an integer from standard input.

 Generating Numbers: range(1, n + 1) produces a sequence of numbers from 1 to n.

 Printing Without Spaces: The * operator unpacks the range into individual arguments for the print function. 

 By setting sep='', the print function concatenates these numbers without any separator, resulting in a continuous string."

"""