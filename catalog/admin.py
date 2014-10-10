from django.contrib import admin

from catalog.models import Publisher

class PublisherAdmin(admin.ModelAdmin):
    pass

admin.site.register(Publisher, PublisherAdmin)