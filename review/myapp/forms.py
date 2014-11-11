from django import forms
from django.contrib.auth.models import User

from .models import Poll, Choice, PollUser


class PollUserForm(forms.ModelForm):

    class Meta:
        model = PollUser
        fields = ('username', 'email', 'password', )


class PollForm(forms.ModelForm):

    class Meta:
        model = Poll
        fields = ('question', 'pub_date', )


class ChoiceForm(forms.ModelForm):

    class Meta:
        model = Choice
        fields = ('poll', 'choice', 'votes', )
