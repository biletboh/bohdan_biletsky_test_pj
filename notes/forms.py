from django import forms 
from notes.models import Notes
from notes.models import Upper 


class NotesForm(forms.Form):
    name = forms.CharField(required=True, label='title', min_length=10, max_length=128)
    body = forms.CharField(required=True, label='content', 
            min_length=10, max_length=1024, 
            widget=forms.Textarea(
                attrs={'placeholder': 'Write your note...',}
                )
            )


class UpperForm(forms.ModelForm):
    class Meta:
        model = Upper
        fields = ['name']
