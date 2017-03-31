from django.conf.urls import url

from . import views


app_name='notes'


urlpatterns = [
        url(r'^$', views.NotesList.as_view(), name = 'notes list'),
        ]