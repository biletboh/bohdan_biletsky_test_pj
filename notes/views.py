from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import FormView 
from django.views.generic import DeleteView 
from django.urls import reverse_lazy
from notes.models import Notes
from notes.forms import NotesForm

class NotesList(ListView):
    model = Notes 
    template_name = 'notes/notes_list.html'


class CreateNotes(FormView):
    template_name = 'notes/create_notes.html'
    form_class = NotesForm
    success_url = '/'

    def form_valid(self, form):
        note = Notes.objects.create(name=form.cleaned_data['name'], body=form.cleaned_data['body'])
        return super(CreateNotes, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(CreateNotes, self).get_context_data(**kwargs)
        context['title'] = 'Create' 
        return context


class UpdateNotes(FormView):
    template_name = 'notes/create_notes.html'
    form_class = NotesForm
    success_url = '/'

    def form_valid(self, form):
        note = Notes.objects.update(name=form.cleaned_data['name'], body=form.cleaned_data['body'])
        return super(UpdateNotes, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(UpdateNotes, self).get_context_data(**kwargs)
        context['title'] = 'Update' 
        return context


class DeleteNotes(DeleteView):
    model = Notes
    success_url = reverse_lazy('notes_list')
