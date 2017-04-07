from django import forms
from notes.models import Notes


class CustomUpperCaseField(forms.CharField):
    """Custom CharField that transform value to upper case."""

    def clean(self, value):
        try:
            return value.upper()
        except:
            raise ValidationError


class NotesForm(forms.Form):
    """The form that handles user input for a note."""

    name = CustomUpperCaseField(
        required=True, label='title', min_length=10, max_length=128)
    body = forms.CharField(
        required=True, label='content', min_length=10, max_length=1024,
        widget=forms.Textarea(
            attrs={'placeholder': 'Write your note...', })
            )
    image = forms.FileField(label='image', required=False)

