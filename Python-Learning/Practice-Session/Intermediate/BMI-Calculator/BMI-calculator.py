"""
Tracking your BMI is a useful way of checking if you’re maintaining a healthy weight.
It’s calculated using a person's weight and height, 
Using this formula: weight / height²
"""

# name = input('Enter your name:')
height = input("Enter your height (in feet and inches, e.g., 6'2\"): ")
weight = float(input('Enter your weight(kgs):'))

class BMICalculator:
    """Class to handle BMI calculation and categorization"""

    def __init__(self,weight,height):
        """Initialize with user-provided weight and height"""
        self.weight = weight
        self.height = height * 0.0254  #.. Convert inches to meters directly to self.height variable



    def calculate_bmi(self):
        """Calculate BMI based on weight and height"""
        #.. Initially used the inches formula so I calculate * 703 
        return self.weight / (self.height ** 2) 
    


    def determine_bmi_category(self,bmi):
        """Determine the BMI category based on BMI value"""
        if bmi < 18.5:
            return "Underweight"
    
        elif 18.5 <= bmi < 25:
            return "Normal weight"
    
        elif 25 <= bmi < 30:
            return "Overweight"
    
        else:
            return "Obesity"
    
    def display_results(self):
        """Calculate BMI, determine the category, and display the results."""
        bmi = self.calculate_bmi()
        category= self.determine_bmi_category(bmi)
        print(f'BMI: {bmi:.2f}')
        print(f"Category:{category}")


#.. Split and convert height into inches
feet, inches = map(int,height.replace('"','').split("'"))
height= feet * 12 + inches        

bmi_calulator = BMICalculator(weight,height)
bmi_calulator.display_results()



# weight = int(input());
# height = float(input());
# x = weight/float(height*height);
# if x < 18.5:
#     print('Underweight')
# if x>=18.5 and x<25:
#     print("Normal")
# if x >= 25 and x < 30:
#    print('Overweight')
# if x >= 30:
#    print('Obesity')
    
