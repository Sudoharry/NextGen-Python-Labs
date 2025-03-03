#.. WAF to find in which line of the file does the word "leaning" occur first. Print -1 if word not found.

## line---> words

# def check_for_line():
#      word = input("Enter the word you want to search:")
#      data = True  #.. if we kee the string to "" the loop won't run.
#      line_no = 1  #.. Line number is initialized as 1.
#      with open("practice.txt", "r") as f:
#           while data:       
#                data = f.readline()
#                if(word in data):
#                    print(line_no) 
#                    return
#                line_no += 1   
#      return -1         

# check_for_line()


#.. From a file containing numbers seprated by comma, print the count of even numbers.

#.. Take the individual numbers first and then parse the number(type casting to integer)

# with open("practice1.txt","r") as f:
#      data = f.read()
#      print(data)


#      num = ""
#      for i in range(len(data)):
#           if(data[i] == ","):
#                print(int(num))
#                num = ""
#           else:
#                num += data[i]

count = 0
with open("practice1.txt","r") as f:
     data = f.read()  #.. we read the data first

     num = data.split(",")  #..  we split the data using seprator
     for val in num:        #.. we used the loop for list using the type cast
          if(int(val) % 2 == 0):
               count += 1
 
print(count)

                   


