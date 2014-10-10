
from django.contrib.auth.models import User

from rest_framework import viewsets
from catalog.models import (Publisher, Dataset, Resource)
from catalog.serializers import (PublisherSerializer,
    DatasetSerializer,
    ResourceSerializer,
    UserSerializer)

class DatasetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows datasets to be viewed or edited.
    """
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer
    lookup_field = 'slug'


class PublisherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows publishers to be viewed or edited.
    """
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    lookup_field = 'slug'

class ResourceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be resources
    """
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be resources
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
