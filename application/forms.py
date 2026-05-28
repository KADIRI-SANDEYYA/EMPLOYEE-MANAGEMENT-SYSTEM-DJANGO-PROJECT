from django import forms
from .models import EmployeeModel


class EmployeeForm(forms.ModelForm):

    class Meta:

        model = EmployeeModel

        fields = '__all__'

        widgets = {

            'employee_id': forms.NumberInput(attrs={
                'class': 'input-field',
                'placeholder': 'Enter Employee ID'
            }),

            'first_name': forms.TextInput(attrs={
                'class': 'input-field',
                'placeholder': 'Enter First Name'
            }),

            'last_name': forms.TextInput(attrs={
                'class': 'input-field',
                'placeholder': 'Enter Last Name'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'input-field',
                'placeholder': 'Enter Email Address'
            }),

            'phone': forms.NumberInput(attrs={
                'class': 'input-field',
                'placeholder': 'Enter Phone Number'
            }),

            'department': forms.Select(attrs={
                'class': 'input-field'
            }),

            'designation': forms.Select(attrs={
                'class': 'input-field'
            }),

            'salary': forms.NumberInput(attrs={
                'class': 'input-field',
                'placeholder': 'Enter Salary'
            }),

            'joining_date': forms.DateInput(attrs={
                'class': 'input-field',
                'type': 'date'
            }),

            'profile_image': forms.FileInput(attrs={
                'class': 'input-field'
            }),

        }