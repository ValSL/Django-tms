from django import forms
from django.core.exceptions import ValidationError


class OrderForm(forms.Form):
    name = forms.CharField(max_length=50)
    from_field = forms.CharField(max_length=50)
    to_field = forms.CharField(max_length=50)
    count_of_people = forms.IntegerField()
    date = forms.DateField(widget=forms.SelectDateWidget, input_formats=['%Y-%m-%d'])

    name.widget.attrs.update({'class': 'form-control col-3'})
    from_field.widget.attrs.update({'class': 'form-control col-3'})
    to_field.widget.attrs.update({'class': 'form-control col-3'})
    count_of_people.widget.attrs.update({'class': 'form-control col-3'})


    def clean_name(self):
        name = self.cleaned_data['name']
        if True in list(map(str.isdigit, name)):
            raise ValidationError('Name must be string!')
        return name
