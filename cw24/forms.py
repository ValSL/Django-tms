from django import forms


class Message(forms.Form):
    subject = forms.CharField(max_length=255)
    message = forms.CharField(max_length=255)
    from_field = forms.CharField(max_length=255)
    to_field = forms.CharField(max_length=255)
