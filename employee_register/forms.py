
from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        # fields = '__all__'
        fields = ('fullname','mobile','emp_code','position')
        widgets = {
            'position': forms.Select(attrs={'class': 'form-select'}),  # Add form-select class
        }
        labels = {
            'fullname' : "Full Name",
            'emp_code' : "Employee Code"
        }
        
        
    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].widget.attrs.update({'class': 'form-select'})  # Add Bootstrap 5 class
        self.fields['position'].empty_label = "Select"
        self.fields['emp_code'].required = False