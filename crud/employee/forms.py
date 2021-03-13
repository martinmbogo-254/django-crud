from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('name', 'email', 'mobile', 'emp_code', 'gender', 'position')


class EmployeeRegister(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
