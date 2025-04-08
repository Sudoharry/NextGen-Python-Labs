from django.db import models
from django.core.exceptions import ValidationError
import re

# Validate the fullname using the regular expression
def validate_fullname(value):
    if not re.match("^[A-Za-z ]+$",value):
        return ValidationError("Please enter character in the name")

# Validate the number with minimum 10 numbers
def validate_mobile(value):
    if not re.match(r"^\d{10}$",value):
        return ValidationError("Mobile number should be equal to 10 number")
    

# Position table object having a foreign key dependency 
class Position(models.Model):
    title = models.CharField(max_length=50)

# For string representation on admin panel
    def __str__(self):
        return self.title


# Employee table object for storing information like fullname, mobile, emp_code and position
class Employee(models.Model):
    fullname= models.CharField(max_length=50, validators=[validate_fullname])
    mobile= models.CharField(max_length=50, validators=[validate_fullname])
    emp_code= models.CharField(max_length=4)
    position= models.ForeignKey(Position, on_delete=models.CASCADE)


# String representation on the database to see fullname
    def __str__(self):
        return self.fullname