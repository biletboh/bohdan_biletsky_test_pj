from django.db import models
from django.utils import timezone
from easy_thumbnails.fields import ThumbnailerImageField


# Custom CharField class that transform the value to UPPER case.

class UpperCaseCharField(models.CharField):

    description = "A field for UPPER case characters."

    def __init__(self, *args, **kwargs):
        super(UpperCaseCharField, self).__init__(*args, **kwargs)
    
    def pre_save(self, model_instance, add):
        value = getattr(model_instance, self.attname).upper()
        setattr(model_instance, self.attname, value)
        return getattr(model_instance, self.attname) 

    def formfield(self, **kwargs):
        from django.forms import CharField
        defaults = {'form_class': CharField}
        defaults.update(kwargs)
        return super(UpperCaseCharField, self).formfield(**defaults)


class Notes(models.Model):
    name = models.CharField(max_length=128)
    body = models.CharField(max_length=3036)
    pub_date = models.DateTimeField(default=timezone.datetime.now)
    image = ThumbnailerImageField(upload_to='media/notes', blank=True) 

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.name


class Books(models.Model):
    name = UpperCaseCharField(max_length=256)
    notes = models.ManyToManyField(Notes)

    def __str__(self):
        return self.name


class Upper(models.Model):
    name = UpperCaseCharField(max_length=256)

    def __str__(self):
        return self.name


class HttpRequest(models.Model):
    time = models.DateTimeField(blank=True, null=True)
    remote_addr = models.CharField(max_length=39, db_index=True)
    req_method = models.CharField(max_length=16)
    req_protocol = models.CharField(max_length=16)
    req_path = models.TextField()
    req_headers_json = models.TextField()
    
    class Meta:
        ordering = ('-time',)

