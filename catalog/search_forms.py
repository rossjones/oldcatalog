from django import forms

from haystack.forms import SearchForm

from catalog.models import (Dataset, Publisher)

class PublisherSearchForm(SearchForm):
    models = [
        Publisher
    ]

    def get_models(self):
        return self.models

    def search(self):
        sqs = super(PublisherSearchForm, self).search().models(Publisher)
        if not self.is_valid():
            return self.no_query_found()
        return sqs

class DatasetSearchForm(SearchForm):
    models = [
        Dataset
    ]

    def get_models(self):
        return self.models

    def search(self):
        sqs = super(DatasetSearchForm, self).search().models(Dataset)
        if not self.is_valid():
            return self.no_query_found()
        return sqs
