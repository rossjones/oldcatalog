from django.dispatch import receiver
from django.db import models
from django.db.models import signals

from autoslug import AutoSlugField

class Dataset(models.Model):

    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title',
        slugify=lambda value: value.replace(' ','-'))
    description = models.TextField()

    def __unicode__(self):
        return self.title

