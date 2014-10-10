from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'catalog.views.app_views.home', name='home'),

    url(r'^publisher/', 'catalog.views.publishers.list', name='publisher_list'),
    url(r'^data/', 'catalog.views.datasets.list', name='dataset_list'),


    url(r'^(?P<slug>[\w-]+)$', 'catalog.views.publishers.show', name='publisher_show'),

    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)