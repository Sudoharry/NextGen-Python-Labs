# The program flows is like, If you're above 18, or equal to 18, then you can apply for a driving licence

age = int(input("Enter your age:"))

# if (age >= 18):
#     print("You're eligble for a Driving Licence.")   # indentation 
# else:
#      print("You're not eligle for Driving Licence")


# print("End of code")



# Nesting


if (age >= 18):
     if (age >=80):
        print("Cannot Drive")
     else:
        print("Can Drive")

else:
    print("Cannot Drive")