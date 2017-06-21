from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
# Create your views here.

def signup(request):
    print "signing up"
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print form
        if form.is_valid():
            print "form is valid"
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/form')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})


def logout(request):
    return render(request, 'logout.html',)

def index(request):
    return render(request, 'index.html',)
