from django import forms
from .models import NatureImage


class ImageForm(forms.ModelForm):
    class Meta:
        model = NatureImage
        fields = ['width', 'height']

        widgets = {
            'width': forms.TextInput(attrs={'class': 'form-control'}),
            'height': forms.TextInput(attrs={'class': 'form-control'}),
        }
