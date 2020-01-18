from django import forms

class CustomerForm(forms.Form):
    firstname = forms.CharField(max_length=255)
    lastname = forms.CharField(max_length=255)
    age = forms.IntegerField()
    profession = forms.CharField(max_length=255)

    firstname.widget.attrs.update({'class': 'form-control'})
    lastname.widget.attrs.update({'class': 'form-control'})
    age.widget.attrs.update({'class': 'form-control'})
    profession.widget.attrs.update({'class': 'form-control'})

    def __str__(self):
        return f'id - {self.id} | name - {self.firstname}'
