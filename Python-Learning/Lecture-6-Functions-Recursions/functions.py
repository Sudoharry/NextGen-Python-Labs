## Create a function which can calculate the average of 3


# def calc_avg(a,b,c):
#     sum = a + b + c
#     avg = sum / 3
#     # print(avg)
#     return avg

# avg_3 = calc_avg(2,3,5) # Create a variable and store the cal_average function and print the variable which passed function as argument
# print(avg_3)



def cal_prod(a=1,b=1):  # In this case, if user doesn't pass any value then function will call the default value.
    print(a*b) # This will print the multiplication of and b
    return(a*b) # This returns the multiplication of a and b


cal_prod(5,5)  # This was argument that we need pass for the multiplication number that we want to calculate.