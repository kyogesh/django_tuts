from django import forms
from django.contrib.auth.models import User

from .models import Poll, PollUser


class PollUserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = PollUser
        fields = ('username', 'email', 'password', )


class PollForm(forms.ModelForm):

    class Meta:
        model = Poll
        fields = ('question', )
