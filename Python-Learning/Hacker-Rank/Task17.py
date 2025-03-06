"""
There is a horizontal row of n cubes. The length of each cube is given. You need to create a new vertical pile of cubes. 
The new pile should follow these directions: if cube[i] is on top of cube[j] then sideLength[j]  >= sideLength[i].

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time.
 Print Yes if it is possible to stack the cubes. Otherwise, print No.

Example

blocks = [1,2,3,8,7]

Result: No

After choosing the rightmost element, 7, choose the leftmost element,1 . After than, the choices are 2 and 8. These are both larger than the top block of size 1.


Result: Yes

Choose blocks from right to left in order to successfully stack the blocks.


Input Format

The first line contains a single integer  T, the number of test cases.
For each test case, there are 2 lines.
The first line of each test case contains n, the number of cubes.
The second line contains n space separated integers, denoting the sideLengths of each cube in that order.



 
"""

#!/bin/python3

import sys

def can_stack_cubes(cubes):
    left, right = 0, len(cubes) - 1
    last_picked = float('inf')  # Initialize with an infinitely large value

    while left <= right:
        if cubes[left] > cubes[right]:  # Pick the larger cube from the left or right
            chosen = cubes[left]
            left += 1
        else:
            chosen = cubes[right]
            right -= 1
        
        if chosen > last_picked:  # Check if the stacking condition is violated
            return "No"
        
        last_picked = chosen  # Update the last picked cube
    
    return "Yes"

# Read input
t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    cubes = list(map(int, sys.stdin.readline().strip().split()))
    print(can_stack_cubes(cubes))
