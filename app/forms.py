from django import forms

from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('fullname','emp_code','mobile','position','address')
        labels={
            'fullname':'Full Name',
            'mobile':'Mobile No',
           
            'emp_code':'Employee Code'
        }


       