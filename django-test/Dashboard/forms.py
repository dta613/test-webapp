from django import forms
from models import Patient
from django.forms import widgets
from datetime import datetime, date
from django.db import models
from django.shortcuts import redirect




class Patient_form(forms.Form):
    Patient_name = forms.CharField(label="Name", max_length=30)
    condition = forms.CharField(widget=forms.TextInput, max_length=30)
    date_input = models.DateTimeField(default=datetime.now, blank=True)

    models = Patient
    fields = ('Patient_name','condition', 'date_input')

    def save(self, commit=True):
        Patient_data = super(Patient_form, self).save(commit=False)
        Patient_data.Patient_name = self.cleaned_data['Patient_name']
        Patient_data.condition = self.cleaned_data['condition']
        if commit:
            Patient_data.save()
            return redirect('dashboard')
        else:
            return redirect('form')


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

#class CommentForm(forms.Form):
#     name = forms.CharField(label='Your name')
#     url = forms.URLField(label='Your website', required=False)
#     comment = forms.CharField()
