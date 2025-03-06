class A:    #. Parent class
    varA= "Welcome to class A"

class B: #. Parent class
    varB = "Welcome to class B"

class C(A,B):   #..All the class have been inherited by C
    varC= "Welcome to class C"

c1 = C()  #. Created a varible for instance of class


print(c1.varC)  #.. We call the class C with varC here which is there within the class C
print(c1.varB)  #.. Also, we inherited the classB varB here, as it was inherited within the argument of classC. So, it will print the C,B,A
print(c1.varA)  #.. Same in the case of varA.