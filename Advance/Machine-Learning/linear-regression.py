"""
The x-axis represents age, and the y-axis represents speed. 
We have registered the age and speed of 13 cars as they were passing a tollbooth.
Let us see if the data we collected could be used in a linear regression:


"""

import matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()
