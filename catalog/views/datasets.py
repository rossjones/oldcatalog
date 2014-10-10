from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.urlresolvers import reverse

from django.http import HttpResponse

from django.shortcuts import (render_to_response,
                              redirect,
                              get_object_or_404)
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt


def list(request):
    return render_to_response('datasets/list.html',
        {},
        context_instance=RequestContext(request))

def show(request, slug):
    pass