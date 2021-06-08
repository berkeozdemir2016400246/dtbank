from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms



def serveLogin(request):
    name = request.POST.get("name")
    surname = request.POST.get("surname")
    loginCheck = checkCreditentials(name, surname)
    if (loginCheck):
        request.session['name'] = name
        return redirect('../home')
    context = {"login_fail": True, "login_form": LoginForm()}
    return render(request, 'ui/login.html', context)

def serveDbManager(request):
    return  render( request, 'ui/dbmanager.html')

def serveUser(request):
    return  render( request, 'ui/user.html')


def checkCreditentials(name, surname):
    if((name == "berke" and surname == "ozdemir")):
        return True
    else:
        return False


class LoginForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Surname'}))