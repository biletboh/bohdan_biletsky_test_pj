import random
import json
from django.http import JsonResponse
from django.shortcuts import render 
from django.core import serializers
from django.views.generic import ListView
from django.views.generic import FormView 
from django.views.generic import DeleteView 
<<<<<<< HEAD
from django.views.generic import TemplateView 
=======
from django.views.generic import View 
>>>>>>> widget
from django.urls import reverse_lazy
from notes.models import Notes, HttpRequest
from notes.forms import NotesForm


class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
            }

            return JsonResponse(data)
        else:
            return response


class NotesList(ListView):
    model = Notes 
    template_name = 'notes/notes_list.html'


class CreateNotes(AjaxableResponseMixin, FormView):
    template_name = 'notes/create_notes.html'
    form_class = NotesForm
    success_url = '/create'

    def form_valid(self, form):
        note = Notes.objects.create(
            name=form.cleaned_data['name'], 
            body=form.cleaned_data['body'])
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
        note = Notes.objects.update(
            name=form.cleaned_data['name'], 
            body=form.cleaned_data['body'])
        return super(UpdateNotes, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(UpdateNotes, self).get_context_data(**kwargs)
        context['title'] = 'Update' 
        return context


class DeleteNotes(DeleteView):
    model = Notes
    success_url = reverse_lazy('notes_list')


class HttpRequestsView(TemplateView):
    template_name = 'notes/requests.html'

    def get(self, request):
        http_requests = HttpRequest.objects.all()[0:10] 
        http_requests_json = serializers.serialize('json', http_requests) 
        if request.is_ajax():
            return JsonResponse(http_requests_json, safe=False)
        return render(request, self.template_name, {
            'http_requests': http_requests_json,
            })


class WidgetView(View):
    def get(self, request):
        notes = Notes.objects.all()
        note_json = serializers.serialize('json', notes) 
        return JsonResponse(note_json, safe=False)
