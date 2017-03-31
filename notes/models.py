from django.db import models
from django.utils import timezone


class Notes(models.Model):
    name = models.CharField(max_length=128)
    body = models.CharField(max_length=1024)
    pub_date = models.DateTimeField(default=timezone.datetime.now)


