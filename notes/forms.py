from django import forms 
from notes.models import Notes


class NotesForm(forms.Form):
    name = forms.CharField(required=True, label='title', min_length=10, max_length=128)
    body = forms.CharField(required=True, label='content', min_length=10, max_length=1024, widget=forms.Textarea)
