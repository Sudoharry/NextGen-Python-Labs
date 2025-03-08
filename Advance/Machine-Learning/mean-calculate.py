

"""
 
 In Machine Learning (and in mathematics) there are often three values that interests us:

 Mean - The average value
 Median - The mid point value
 Mode - The most common value

 We have registered the speed of 13 cars:


"""
"""
To calculate the mean, find the sum of all values, and divide the sum by the number of values:

"""

import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)

print(x)