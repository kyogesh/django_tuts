from .models import Person
from django import forms

class PersonForm(forms.ModelForm):

    class Meta:

        model = Person
        fields = ['name', 'birth_date', 'birth_place',]
