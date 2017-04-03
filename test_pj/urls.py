from django.conf.urls import url
from django.conf.urls import include 
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('notes.urls')),
    url(r'^upload/', include('django_file_form.urls')),
]
