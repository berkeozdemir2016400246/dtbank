from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
import pymysql


def serveLogin(request):
    name = request.POST.get("name")
    surname = request.POST.get("surname")
    userType = request.POST.get("userType")
    loginCheck = checkCreditentials(name, surname)
    if(userType == "dbmanager"):
        if (loginCheck):
            return redirect('../dbmanager')
    else:
        if (loginCheck):
            return redirect('../user')
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
    userType = forms.CharField(widget=forms.Select(choices=[('dbmanager','Database Manager'), ('user','User')]))

class CreateUserForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    instituteName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Institute Name'}))
    password =  forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password'}))
    postType = '1'

class DeleteDrugForm(forms.Form):
    drugId = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Drug Id'}))
    postType = 2

class UpdateDrugForm(forms.Form):
    drugId = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Drug Id'}))
    affinity = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Affinity'}))

class DeleteProteinForm(forms.Form):
    proteinId = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Protein Id'}))

class UpdateContributorsForm(forms.Form):
    reactionId = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Reaction Id'}))
    contributors = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Contributors'}))


def serveCreateUser(request):
    context = {"user_create_form": CreateUserForm()}
    return  render( request, 'ui/dbmanagertemplates/createuser.html', context)


def serveDeleteDrug(request):
    context = { "delete_drug_form": DeleteDrugForm()}
    return render(request, 'ui/dbmanagertemplates/deletedrug.html', context)


def serveUpdateDrug(request):
    context = {"update_drug_form": UpdateDrugForm()}
    return render(request, 'ui/dbmanagertemplates/updatedrug.html', context)


def serveDeleteProtein(request):
    context = { "delete_protein_form": DeleteProteinForm()}
    return render(request, 'ui/dbmanagertemplates/deleteprotein.html', context)


def serveUpdateReaction(request):
    context = { "update_contributors_form": UpdateContributorsForm}
    return render(request, 'ui/dbmanagertemplates/updatereaction.html', context)