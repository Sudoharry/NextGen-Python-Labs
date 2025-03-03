#. Create a new file "practice.txt" using python. Add the following data in it:

# WAF that replace all the occurences of "java" with "python" in above files.

# Search if the word "learning" exits in the file


# with open("practice.txt","w") as f:

#  f.write("Hi everyone. \nWe are learning File I/O using Java \nI like programming in Java.")
 

#.. Read mode only

# with open("practice.txt", "r") as f:
#     data = f.read()

# new_data = data.replace("Java", "Python")    
# print(new_data)


#.. Once it's check on the read mode, we can overwrite it.

# with open("practice.txt", "r") as f:
#     data = f.read()

# new_data = data.replace("Java", "Python")    
# print(new_data)

# with open("practice.txt", "w") as f:
#     f.write(new_data)



#.. Search the word learning from the practice.txt file 


def check_for_word():
    word = input("Enter the word you want search from the file:")
    with open("practice.txt", "r") as f:
        data = f.read()
        if(data.find(word) != -1):  #  we can use this if(word in data) instead of "data.find(word) != -1 "
          print("Found")
        else:
          print("Not Found")
     
check_for_word()
