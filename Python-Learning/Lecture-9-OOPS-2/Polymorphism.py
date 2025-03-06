class Complex:
    def __init__(self, real,img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +",self.img,"j")


    def __add__(self, num2):    #.. dunder method is used here and now we can add the complex numbers, earlier without it we did't used it
        # Adding real and imaginary parts
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, + newImg)
    
    def __sub__(self, num2):
        # Subtracting real and imaginary parts
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)



# Creating first complex number (1 + 3j)
num1 = Complex(4,6)
num1.showNumber()            


# Creating second complex number (4 + 6j)
num2 = Complex(1,3)
num2.showNumber()     


# num3 = num1 + num2
# num3.showNumber()

num4 = num1 - num2
num4.showNumber()
# Adding num1 and num2 -> (1+4) + (3+6)j = 5 + 9j
# num3 = num1.add(num2)
# num3.showNumber()