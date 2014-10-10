
from rest_framework import viewsets
from catalog.serializers import (PublisherSerializer, DatasetSerializer, ResourceSerializer)
from catalog.models import (Publisher, Dataset, Resource)

class DatasetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows datasets to be viewed or edited.
    """
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer


class PublisherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows publishers to be viewed or edited.
    """
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class ResourceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be resources
    """
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer