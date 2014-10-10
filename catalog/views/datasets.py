from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import (render_to_response,
                              redirect,
                              get_object_or_404)
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from haystack.query import SearchQuerySet

from catalog.search_forms import DatasetSearchForm
from catalog.models import (Publisher, Dataset)

def list(request):
    form = DatasetSearchForm(request.GET or None)

    search_results = form.search()

    page = request.GET.get('page')
    paginator = Paginator(search_results, 1)
    try:
        publishers = paginator.page(page)
    except PageNotAnInteger:
        publishers = paginator.page(1)
    except EmptyPage:
        publishers = paginator.page(paginator.num_pages)

    total = search_results.count()

    return render_to_response('datasets/list.html',
        {
            'form': form,
            'datasets': publishers,
            'total': total,
        },
        context_instance=RequestContext(request))

def show(request, publisher_slug, slug):

    publisher = get_object_or_404(Publisher, slug=publisher_slug)
    try:
        dataset = Dataset.objects.get(slug=slug, publisher=publisher)
    except Dataset.DoesNotExist:
        raise HttpResponseNotFound()

    return render_to_response('datasets/show.html',
        {
            'publisher': publisher,
            'dataset': dataset
        },
        context_instance=RequestContext(request))
