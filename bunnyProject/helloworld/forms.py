from django import forms
from django.forms import ModelForm, TextInput 
from .models import Name,UserTable

class NameForm(ModelForm):
    class Meta:
        model = Name
        fields = ("name","description")

class UserTableForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = UserTable
        fields = '__all__'

        