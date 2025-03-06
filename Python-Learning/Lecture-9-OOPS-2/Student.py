class Student:
    def __init__(self, phy, math, sci):
        self.phy = phy
        self.math = math
        self.sci = sci

    # def calcPercentage(self):
    #     self.percentage = str((self.phy + self.math + self.sci) / 3) + "%"

    @property  #.. using this property decorator we don't have to calPercentage as it's already been done by the property method.
    def percentage(self):  #.. it will automatically get reflected once there is any change in the parameter. We will get the latest
        return str((self.phy + self.math + self.sci) / 3) + "%"


stu1 = Student(98,97,99)
print(stu1.percentage)

stu1.phy = 86
# print(stu1.phy)
# stu1.calcPercentage()
print(stu1.percentage)
