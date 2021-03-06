from django.conf.urls import url

from . import views


app_name = 'notes'


"""Patterns that maps notes views to urls."""

urlpatterns = [
        url(r'^$', views.NotesList.as_view(), name='notes_list'),
        url(r'^create/$', views.CreateNotes.as_view(),
            name='create_notes'),
        url(r'^(?P<pk>[0-9]+)/update/$', views.UpdateNotes.as_view(),
            name='update_notes'),
        url(r'^(?P<pk>[0-9]+)/delete/$', views.CreateNotes.as_view(),
            name='delete_notes'),
        url(r'^requests/$', views.HttpRequestsView.as_view(),
            name='requests'),
        url(r'^(?P<pk>[0-9]+)/delete/$', views.CreateNotes.as_view(), name='delete_notes'),
        url(r'^widget/$', views.WidgetView.as_view(), name='widget'), 
        ]

