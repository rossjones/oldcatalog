from django.dispatch import receiver
from django.db import models
from django.db.models import signals

from autoslug import AutoSlugField

from .dataset import Dataset

class Resource(models.Model):

    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title',
        unique_with=['dataset__slug'])
    description = models.TextField()

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    mimetype = models.CharField(max_length=200, null=True)
    format   = models.CharField(max_length=200, null=True)
    url      = models.CharField(max_length=200, null=True)
    size     = models.IntegerField(default=0)

    dataset = models.ForeignKey(Dataset, related_name='resources')

    def __unicode__(self):
        return self.title
