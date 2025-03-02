## Figure out a way to store 9 and 9.0 as separate values in the set. (You can take help of built in data types)


# values = {9, '9.0'}
# print(values)



values = {

    ("float", 9.0),
    ("int", 9)
}

print(values)


## Solution1: As 9 and 9.0 both are same, if we need to store it both the values than the first solution is we can use "9.0", "9" as string type. 
##             This way we can store both the values.


## Solution2: We can add both the values in the tuple, and using key value pair, we can assign 9 as a integer and 9.0 as a float this way we can store the data.


