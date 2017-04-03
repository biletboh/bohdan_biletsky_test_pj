from django import forms 
from notes.models import Notes
from notes.models import Upper 
from django_file_form.forms import FileFormMixin, UploadedFileField


class NotesForm(FileFormMixin, forms.Form):
    name = forms.CharField(required=True, label='title', min_length=10, max_length=128)
    body = forms.CharField(required=True, label='content', 
            min_length=10, max_length=1024, 
            widget=forms.Textarea(
                attrs={'placeholder': 'Write your note...',}
                )
            )
    image = UploadedFileField(label='image', required = False)
    form_id = forms.CharField(widget = forms.HiddenInput(), required = False)
    upload_url = forms.CharField(widget = forms.HiddenInput(), required = False)
    delete_url = forms.CharField(widget = forms.HiddenInput(), required = False)
    object_id = forms.CharField(widget = forms.HiddenInput(), required = False)


class UpperForm(forms.ModelForm):
    class Meta:
        model = Upper
        fields = ['name']
