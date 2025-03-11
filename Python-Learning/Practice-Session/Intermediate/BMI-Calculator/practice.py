height = input("Enter the height:")
weight= float(input("Enter the weight:"))

class BMICalculator:
    def __init__(self,weight,height):
        self.weight = weight
        self.height = height * 0.0254  #.. Convert the height from feet into inches

    def calculate_bmi(self):
        return self.weight / (self.height ** 2)


    def determine_bmi_category(self,bmi):
        if bmi < 18.5:
            return "Under Weight"
        
        elif 18.5 <= bmi < 25:
            return "Healthy"

        elif 25 <= bmi < 30:
            return "Over Weight"

        else:
            return "Obesity"

    def display_result(self):
        bmi= self.calculate_bmi()
        category = self.determine_bmi_category(bmi)
        print(f'BMI: {bmi:.2f}')
        print(f'Category: {category}')

feet, inches = map(int,height.replace('"','').split("'"))
height = feet * 12 + inches


bmi_calculator = BMICalculator(weight,height)
bmi_calculator.display_result()


