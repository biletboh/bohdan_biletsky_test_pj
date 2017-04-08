from django.db import models
from django.utils import timezone
from easy_thumbnails.fields import ThumbnailerImageField


class Notes(models.Model):
    """The model for notes."""

    name = models.CharField(max_length=128)
    body = models.CharField(max_length=3036)
    pub_date = models.DateTimeField(default=timezone.datetime.now)
    image = ThumbnailerImageField(upload_to='media/notes', blank=True) 

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.name


class Books(models.Model):
    """The model for Books that store notes."""

    name = models.CharField(max_length=128)
    notes = models.ManyToManyField(Notes)

    def __str__(self):
        return self.name


class HttpRequestStorage(models.Model):
    """The model that stores HttpRequests."""

    time = models.DateTimeField(blank=True, null=True)
    remote_addr = models.CharField(max_length=39, db_index=True)
    req_method = models.CharField(max_length=16)
    req_protocol = models.CharField(max_length=16)
    req_path = models.TextField()
    req_headers_json = models.TextField()
    
    class Meta:
        ordering = ('-time',)

