from django.dispatch import receiver
from django.db import models
from django.db.models import signals

from autoslug import AutoSlugField

class Publisher(models.Model):

    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title',
        slugify=lambda value: value.replace(' ','-'))
    description = models.TextField()

    def __unicode__(self):
        return self.title

"""
    "contact-phone": "",
    "abbreviation": "TD",
    "foi-email": "",
    "id": "72155ce7-f3b4-4211-9175-6c86703d7e6c",
    "description": "Transport Direct offers information for door-to-door travel for both public transport and car journeys around Britain. \r\n\r\nTransport Direct works together with both public and private travel operators and local/national government. Transport Direct is operated by a consortium, led by Atos. The non-profit service is funded by the UK Department for Transport, the Welsh Assembly Government and the Scottish Government.\r\n\r\nhttp://www.transportdirect.info/Web2/Home.aspx?&repeatingloop=Y\r\n\r\n",
    "approval_status": "pending",
    "foi-web": "",
    "users": [
        {
            "capacity": "admin",
            "name": "user_d217"
        },
        {
            "capacity": "editor",
            "name": "user_d32101"
        },
        {
            "capacity": "editor",
            "name": "user_d354621"
        },
        {
            "capacity": "admin",
            "name": "user_d46221"
        },
        {
            "capacity": "admin",
            "name": "user_d5079"
        }
    ],
    "contact-email": "",
    "tags": [ ],
    "foi-name": "",

    "contact-name": "transportdirect.info contact",
    "image_display_url": "",
    "extras": [
        {
            "value": "TD",
            "key": "abbreviation"
        },
        {
            "value": null,
            "key": "category"
        },
        {
            "value": "",
            "key": "contact-email"
        },
        {
            "value": "transportdirect.info contact",
            "key": "contact-name"
        },
        {
            "value": "",
            "key": "contact-phone"
        },
        {
            "value": "",
            "key": "foi-email"
        },
        {
            "value": "",
            "key": "foi-name"
        },
        {
            "value": "",
            "key": "foi-phone"
        },
        {
            "value": "",
            "key": "foi-web"
        },
        {
            "value": "transportdirect.info",
            "key": "website-name"
        },
        {
            "value": "http://www.transportdirect.info/",
            "key": "website-url"
        }
    ],
    "image_url": "",
    "foi-phone": ""

}
"""