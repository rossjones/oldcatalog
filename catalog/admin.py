from django.contrib import admin

from catalog.models import (Dataset, Publisher)

class PublisherAdmin(admin.ModelAdmin):
    pass


class DatasetAdmin(admin.ModelAdmin):
    pass

admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Dataset, DatasetAdmin)