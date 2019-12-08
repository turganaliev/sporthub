from django import forms
from .models import PoleImage, Pole


class FieldCreateForm(forms.ModelForm):
    class Meta:
        model = Pole
        fields = ['title','body']

class FieldImageCreateForm(forms.ModelForm):
    class Meta:
        model = PoleImage
        fields = ['image']
