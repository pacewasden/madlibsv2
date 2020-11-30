from django import forms
from .models import Words

class WordForm(forms.ModelForm):
    class Meta:
        model = Words
        fields = ['verb', 'sport', 'person','action','adjective',
        'place','school','city','athlete', 'expression']