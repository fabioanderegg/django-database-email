from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class EMail(models.Model):
    subject = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.subject
