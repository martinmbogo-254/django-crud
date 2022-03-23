from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Employee, Item, Antivirus



# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ('username','email','password1','password2')

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('name', 'email', 'mobile', 'emp_code', 'gender', 'position')


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields =()

class AntivirusForm(forms.Form):
    class Meta:
        model= Antivirus
        fields=('antivirus_id','officer_name','department','directorate','comp_serial_no')