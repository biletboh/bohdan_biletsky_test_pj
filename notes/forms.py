from django import forms 
from notes.models import Notes


class NotesForm(forms.Form):
    name = forms.CharField(label='title', min_length=10, max_length=128)
    body = forms.CharField(label='content', min_length=10, max_length=1024)
