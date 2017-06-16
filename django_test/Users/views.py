from django.shortcuts import render, redirect
from Users.forms import UserProfileForm
from Users.forms import RegisterForm
from django.contrib.auth import forms
from django.views.generic import View
from django.contrib.auth import login, authenticate, forms, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


import json
# Create your views here.


class Register(View):
	form = RegisterForm
	def get(self, request):
		context = {'form': self.form()}
		return render(request, 'Users/register.html', context)
	def post(self, request):
		form = self.form(request.POST)
		if form.is_valid():
			form.save()

			username = request.POST['username']
			password = request.POST['password1']
			user = authenticate(username=username, password=password)

			login(request, user)


			print(request.POST['name'])

			namedict = '{"name": "%s" }' % request.POST['name']
			print(namedict)

			jsonname = json.loads(namedict)
			print(jsonname)

			userform = UserProfileForm(jsonname, instance=request.user.profile)

			if userform.is_valid():
				userform.save()

				return HttpResponseRedirect('Users/login.html')
			else:
				context = {'form': form}
				return render(request, 'Users/register.html', context)


		else:
			context = {'form': form}
			return render(request, 'Users/register.html', context)




class Login(View):
	form = forms.AuthenticationForm
	def get(self, request):
		context = {'form': self.form()}
		return render(request, 'Users/login.html', context)
	def post(self, request):
		form = self.form(None, request.POST)
		context = {'form': form}
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)

				return HttpResponseRedirect('/')
			else:
				return render(request, 'Users/login.html', context)
		else:
			return render(request, 'Users/login.html', context)

class Logout(View):
	def get(self, request):
		logout(request)
		return redirect('/login')
