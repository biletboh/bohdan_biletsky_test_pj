from django.shortcuts import render
from django.views.generic import ListView
from notes.models import Notes


class NotesList(ListView):
    """View that renders list of notes."""

    model = Notes 
    template_name = 'notes/notes_list.html'

