from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormName(UserCreationForm):

    YEARS= [x for x in range(1980,2021)]
    date_of_birth=forms.DateField(label='Date of birth',widget=forms.SelectDateWidget(years=YEARS))
    email=forms.EmailField()

    class Meta:
        model = User
        fields=["username","email","date_of_birth","password1","password2"]
