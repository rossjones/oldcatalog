from django import forms

from haystack.forms import SearchForm

from catalog.models import Publisher

class PublisherSearchForm(SearchForm):
    models = [
        Publisher
    ]

    def get_models(self):
        return self.models

    def search(self):
        sqs = super(PublisherSearchForm, self).search(search_model=Publisher)
        return sqs

