from django.db import models
from django.utils import timezone

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
    body = models.CharField(max_length=1024)
    pub_date = models.DateTimeField(default=timezone.datetime.now)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.name


class Upper(models.Model):
    name = UpperCaseCharField(max_length=128)

    def __str__(self):
        return self.name



