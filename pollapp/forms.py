from django import forms
from django.forms import inlineformset_factory

from pollapp.models import Poll, Variant

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['title', 'text']

CreatePollFormset = inlineformset_factory(Poll, Variant, extra=10, fields=['text'], can_delete=False)