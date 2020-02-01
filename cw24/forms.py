from django import forms


class Message(forms.Form):
    subject = forms.CharField(max_length=255)
    message = forms.CharField(max_length=255)
    from_field = forms.CharField(max_length=255)
    to_field = forms.CharField(max_length=255)


ANIMALS = (
    ('1', 'Dog'),
    ('2', 'Cat')
)

IMAGE_TYPES = (
    ('1', 'jpg'),
    ('2', 'png'),
    ('3', 'gif'),
)


class FindForm(forms.Form):
    animal = forms.ChoiceField(choices=ANIMALS)
    image_type = forms.ChoiceField(choices=IMAGE_TYPES)
