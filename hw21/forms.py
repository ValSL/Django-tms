from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'age', 'profession']

        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control col-3'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control col-3'}),
            'age': forms.NumberInput(attrs={'class': 'form-control col-3'}),
            'profession': forms.TextInput(attrs={'class': 'form-control col-3'}),
        }
