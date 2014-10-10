from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from catalog.views import api_views

admin.autodiscover()

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', api_views.UserViewSet)
router.register(r'groups', api_views.GroupViewSet)

urlpatterns = patterns('',
    # Examples:

    url(r'^api/', include(router.urls)),
    url(r'^$', 'catalog.views.app_views.home', name='home'),


    url(r'^publisher/(?P<slug>[\w-]+)$', 'catalog.views.publishers.show', name='publisher_show'),
    url(r'^dataset/(?P<slug>[\w-]+)$',
            'catalog.views.datasets.show', name='dataset_show'),

    url(r'^publisher/$', 'catalog.views.publishers.list', name='publisher_list'),
    url(r'^data/$', 'catalog.views.datasets.list', name='dataset_list'),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)