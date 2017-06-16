from django import forms
from models import Patient
from django.forms import widgets
from datetime import datetime, date
from django.db import models


class CommentForm(forms.Form):
     name = forms.CharField(label='Your name')
     url = forms.URLField(label='Your website', required=False)
     comment = forms.CharField()

class Patient_form(forms.Form):
    Patient_name = forms.CharField(label="Name", max_length=30)
    initial_visit = forms.DateField(label="Initial Visit Date")
    condition = forms.CharField(widget=forms.TextInput, max_length=30)
    date_input = models.DateTimeField(default=datetime.now, blank=True)

    model = Patient
    fields = ('Patient_name','initial_visit','condition')

    def save(self, commit=True):
        Patient_data = super(Patient_form, self).save(commit=False)
        Patient_data.Patient_name = self.cleaned_data['Patient_name']
        Patient_data.initial_visit = self.cleaned_data['initial_visit']
        Patient_data.condition = self.cleaned_data['condition']
        if commit:
            Patient_data.save()
            return Patient_data

# class RegisterForm(UserCreationForm):
# 	email = forms.EmailField(label="Email Address")
	# name = forms.CharField(label="Name")
# 	class Meta:
# 		model = User
# 		fields = ('name','username','email', 'password1', 'password2')
# 	def save(self, commit=True):
# 		user = super(RegisterForm, self).save(commit=False)
# 		user.email = self.cleaned_data['email']
# 		user.name = self.cleaned_data['name']
# 		user.set_password(self.cleaned_data['password1'])
# 		if commit:
# 			user.save()
# 			return user
