height_inches = float(input("Enter your height:"))
weight = input("Enter your weight")

class BMICalculator:
    """This BMICalculator class is a container for conversion and categorization"""
    def __init__(self, height_inches,weight):
        self.height = height_inches * 0.0254 #.. This will convert feet into inches 
        self.weight = weight


    def calculate_bmi(self):
        return self.weight / self.height_inches ** 2 #.. Based on the BMI calculation    


    def determine_BMI_category(bmi):    
        if bmi < 18:
            return "Under Weight"
        elif 18 <= bmi <=25:
            return "Normal Weight"
        elif 25 < bmi <=30:
            return "Over Weight"
        else:
            return "Obese"
        

    def display_result(self):
        bmi = self.calculate_bmi()
        category = self.determine_BMI_category(bmi)
        print('BMI: {bmi.2f}')


    inches,feet = map((height.replace("'",'').split('"')))
    height = 12 * feet + inches


bmi_calculator = BMICalculator (weight, height_inches)    
bmi_calculator.display_result()
