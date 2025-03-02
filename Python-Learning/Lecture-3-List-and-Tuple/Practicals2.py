## WAP to check if a list contains a palindrome of elements. (Hint: Use copy() method)

list1 = [1, 2, 1]
list2 = ["m", "a","a", "m"]
list3 = [1, 2, 3]

copy_list2 = list2.copy()
copy_list2.reverse()


if (copy_list2 == list2):
     print ("Palidrome")
else:
     print ("Not Palidrome")     