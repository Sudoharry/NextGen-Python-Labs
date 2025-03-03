## Read a file using the open(), read(), close()
# a = means add in the end
# w = it will overwrite the existing text.
# 
f = open("demo.txt","a")

# data = f.read()
# print(data)


f.write("\nI'm unable to read the second line using the readline function in file IO") #.. this will overwrite the existing text file and add new line

# print(type(data))
f.close()