from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedRelatedField

from catalog.models import (Publisher, Dataset, Resource)

class PublisherSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Publisher
        fields = ('slug', 'title', 'description', 'datasets')


class DatasetSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Dataset
        fields = ('slug', 'title', 'description', 'publisher', 'resources')


class ResourceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Resource
        fields = ('slug', 'title', 'description', 'url', 'dataset')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username', 'email')
        lookup_field = 'username'
