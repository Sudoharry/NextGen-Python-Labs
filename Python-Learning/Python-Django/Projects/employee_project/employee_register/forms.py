
from django import forms
from .models import Employee
import re

class EmployeeForm (forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('fullname', 'emp_code', 'mobile', 'position')
        labels = {
            'fullname': 'Full Name',
            'emp_code': 'EMP. Code',
            'mobile': 'Mobile',
            'position': 'Position'
        }
    
     
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['emp_code'].required = False

class EmployeeUploadForm(forms.Form):
    csv_file = forms.FileField(label="Upload CSV File")   