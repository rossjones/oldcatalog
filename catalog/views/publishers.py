from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import (render_to_response,
                              redirect,
                              get_object_or_404)
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from haystack.query import SearchQuerySet

from catalog.search_forms import PublisherSearchForm
from catalog.models import Publisher


def list(request):
    form = PublisherSearchForm(request.GET or None)

    search_results = form.search()

    page = request.GET.get('page')
    paginator = Paginator(search_results, 1)
    try:
        publishers = paginator.page(page)
    except PageNotAnInteger:
        publishers = paginator.page(1)
    except EmptyPage:
        publishers = paginator.page(paginator.num_pages)

    total = paginator.count

    return render_to_response('publishers/list.html',
        {
            'form': form,
            'publishers': publishers,
            'total': total,
        },
        context_instance=RequestContext(request))


def show(request, slug):

    publisher = get_object_or_404(Publisher, slug=slug)

    return render_to_response('publishers/show.html',
        {
            'publisher': publisher,
        },
        context_instance=RequestContext(request))
