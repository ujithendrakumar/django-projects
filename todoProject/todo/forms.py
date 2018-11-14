from   django.forms import ModelForm, TextInput
from .models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['name']
        widgets = {'name':TextInput(attrs={'class':"form-control", 'placeholder':"Todo Title","autofocus":'true'})}
