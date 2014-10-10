from django.dispatch import receiver
from django.db import models
from django.db.models import signals

from autoslug import AutoSlugField

from .publisher import Publisher

class Dataset(models.Model):

    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    description = models.TextField()

    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True)

    temporal_coverage_from = models.DateTimeField(null=True, blank=True)
    temporal_coverage_to = models.DateTimeField(null=True, blank=True)

    published = models.BooleanField(default=False)

    publisher = models.ForeignKey(Publisher, related_name='datasets')

    def __unicode__(self):
        return self.title

"""
"license_title": "UK Open Government Licence (OGL)",
"maintainer": null,
"author": "Transport Direct",
"author_email": "",

"maintainer_email": null,

"foi-email": "",
    "temporal_granularity": "day",
    "geographic_coverage": [
        "england",
        "scotland",
        "wales"
    ],
"license_id": "uk-ogl",
"foi-web": "",
"unpublished": "false",
        "resources": [
            {
                "mimetype": "text/html",
                "cache_url": "http://data.gov.uk/data/resource_cache/f2/f2556c38-c68f-4288-aa58-91ef9eef46cb/resource",
                "hash": "257eac5eb8dc5fbb6893e611c6bca30b89895d78",
                "description": "NaPTAN home page on DfT website (for background information)",
                "format": "HTML",
                "url": "http://www.dft.gov.uk/naptan/",
                "cache_last_updated": "2013-06-19T04:36:54.403838",
                "cache_filepath": "/mnt/shared/ckan_resource_cache/f2/f2556c38-c68f-4288-aa58-91ef9eef46cb/resource",
                "tracking_summary": {
                    "total": 0,
                    "recent": 0
                },
                "last_modified": "2014-02-15T06:24:00.473683",
                "position": 0,
                "revision_id": "fb79b999-9721-4b93-8628-104ab0a6a687",
                "id": "f2556c38-c68f-4288-aa58-91ef9eef46cb",
                "resource_type": "file",
                "size": 12014
            },
            {
                "mimetype": "text/xml",
                "cache_url": "http://data.gov.uk/data/resource_cache/77/77d4437f-fc27-424f-a18c-e308b81475e7/NaPTAN-metadata.xml",
                "hash": "054da2c7e61e077077c81c9a981c1fd8e1df7a94",
                "description": "Meta-data",
                "format": "XML",
                "url": "http://www.dft.gov.uk/NaPTAN/snapshot/NaPTAN-metadata.xml",
                "cache_last_updated": "2013-06-19T19:47:22.977295",
                "cache_filepath": "/mnt/shared/ckan_resource_cache/77/77d4437f-fc27-424f-a18c-e308b81475e7/NaPTAN-metadata.xml",
                "tracking_summary": {
                    "total": 0,
                    "recent": 0
                },
                "last_modified": "2014-05-10T04:25:32.563970",
                "position": 1,
                "revision_id": "7d5e8e05-6e17-48a4-b879-e5b52dc8a4b7",
                "id": "77d4437f-fc27-424f-a18c-e308b81475e7",
                "resource_type": "file",
                "size": 3035
            },
            {
                "mimetype": "application/x-zip-compressed",
                "cache_url": "http://data.gov.uk/data/resource_cache/e3/e3d0c00c-abb7-4159-b512-5e3ac394780a/NaPTANcsv.zip",
                "hash": "1b6b5a06f43e016f5553ef16330ef943bbba0f19",
                "description": "Zipped CSV format",
                "format": "CSV",
                "url": "http://www.dft.gov.uk/NaPTAN/snapshot/NaPTANcsv.zip",
                "cache_last_updated": "2013-06-19T19:47:59.323345",
                "cache_filepath": "/mnt/shared/ckan_resource_cache/e3/e3d0c00c-abb7-4159-b512-5e3ac394780a/NaPTANcsv.zip",
                "tracking_summary": {
                    "total": 0,
                    "recent": 0
                },
                "last_modified": "2014-05-10T04:25:48.841828",
                "position": 2,
                "revision_id": "9b24e4a2-e1c8-4752-9779-b2f697880bd4",
                "id": "e3d0c00c-abb7-4159-b512-5e3ac394780a",
                "resource_type": "file",
                "size": 27658214
            },
            {
                "mimetype": "application/x-zip-compressed",
                "cache_url": "http://data.gov.uk/data/resource_cache/d6/d6dcb728-844b-45b9-a3cb-3db07dd50701/NaPTANxml.zip",
                "hash": "32f2fdb431755c07e204a92165a3c8a153556730",
                "description": "Zipped XML format",
                "format": "XML",
                "url": "http://www.dft.gov.uk/NaPTAN/snapshot/NaPTANxml.zip",
                "cache_last_updated": "2013-06-19T19:48:30.486601",
                "cache_filepath": "/mnt/shared/ckan_resource_cache/d6/d6dcb728-844b-45b9-a3cb-3db07dd50701/NaPTANxml.zip",
                "tracking_summary": {
                    "total": 0,
                    "recent": 0
                },
                "last_modified": "2014-05-10T04:25:51.133300",
                "position": 3,
                "revision_id": "c3ab6c95-e139-4406-b661-8a2f42444683",
                "id": "d6dcb728-844b-45b9-a3cb-3db07dd50701",
                "resource_type": "file",
                "size": 33440993
            },
            {
                "hash": "",
                "description": "GTFS format",
                "created": "2014-06-12T15:23:06.021769",
                "url": "http://www.dft.gov.uk/NaPTAN/snapshot/GTFS.zip",
                "format": "ZIP",
                "tracking_summary": {
                    "total": 0,
                    "recent": 0
                },
                "position": 4,
                "revision_id": "a64d7694-c07f-4f41-9fac-cdc3f7c097a2",
                "id": "88428c00-bf0f-46e9-8aec-434b0f9f5757",
                "resource_type": "file"
            }
        ],
        "creator_user_id": null,
        "num_resources": 5,
        "contact-email": "",
        "tags": [
            {
                "vocabulary_id": null,
                "display_name": "Transportation",
                "name": "Transportation",
                "revision_timestamp": "2012-07-04T08:02:15.122990",
                "state": "active",
                "id": "423aad62-c714-45b6-9f9b-1b8fe4933ae1"
            },
            {
                "vocabulary_id": null,
                "display_name": "airplane",
                "name": "airplane",
                "revision_timestamp": "2010-03-19T17:59:21.466804",
                "state": "active",
                "id": "faae07ae-31cb-47fe-82a4-ac4585b69f68"
            },
            {
                "vocabulary_id": null,
                "display_name": "airport",
                "name": "airport",
                "revision_timestamp": "2010-03-19T17:59:21.466804",
                "state": "active",
                "id": "30073445-2cd6-41ce-8c19-2963a6768bd2"
            },
            {
                "vocabulary_id": null,
                "display_name": "bus",
                "name": "bus",
                "revision_timestamp": "2010-03-19T17:59:21.466804",
                "state": "active",
                "id": "985621e7-82e2-47e3-9ae2-166b2ddf88a8"
            },
            {
                "vocabulary_id": null,
                "display_name": "bus-station",
                "name": "bus-station",
                "revision_timestamp": "2010-03-19T17:59:21.466804",
                "state": "active",
                "id": "9b6c8d30-d4ce-4fcd-a29d-4b0ac0eaf513"
            },
            {
                "vocabulary_id": null,
                "display_name": "bus-stop",
                "name": "bus-stop",
                "revision_timestamp": "2010-03-19T17:59:21.466804",
                "state": "active",
                "id": "c1c4182d-c456-4750-b121-4e8cf8b4e511"
            },
            {
                "vocabulary_id": null,
                "display_name": "easting-northing",
                "name": "easting-northing",
                "revision_timestamp": "2010-03-19T17:59:21.466804",
                "state": "active",
                "id": "5487fea4-24eb-4737-a968-ba06266abf18"
            },
            {
                "vocabulary_id": null,
                "display_name": "ferry",
                "name": "ferry",
                "revision_timestamp": "2010-03-19T17:59:21.466804",
                "state": "active",
                "id": "56412d34-02ef-4b89-a59f-af84fea08884"
            },
            {
                "vocabulary_id": null,
                "display_name": "light-rail",
                "name": "light-rail",
                "revision_timestamp": "2010-03-19T17:59:21.466804",
                "state": "active",
                "id": "adcfcbcc-763f-4f13-a801-747eaec81c4a"
            },
            {
                "vocabulary_id": null,
                "display_name": "local-authority",
                "name": "local-authority",
                "revision_timestamp": "2010-03-19T17:59:21.466804",
                "state": "active",
                "id": "f52dac78-36e3-4261-b361-75315980e529"
            },
            {
                "vocabulary_id": null,
                "display_name": "local-authority-administrative-area",
                "name": "local-authority-administrative-area",
                "revision_timestamp": "2010-03-19T17:59:21.466804",
                "state": "active",
                "id": "86cfa7b8-5a9b-4b93-a5d4-e09e4e12e3b9"
            },
            {
                "vocabulary_id": null,
                "display_name": "location",
                "name": "location",
                "revision_timestamp": "2010-03-19T17:59:21.466804",
                "state": "active",
                "id": "9584ba51-b00c-41b6-9cc5-6a10e25d9a07"
            },
            {
                "vocabulary_id": null,
                "display_name": "metro",
                "name": "metro",
                "revision_timestamp": "2010-03-19T17:59:21.466804",
                "state": "active",
                "id": "70429a63-0831-4b53-aea6-b5b4330da962"
            },
            {
                "vocabulary_id": null,
                "display_name": "ordnance-survey-grid-reference",
                "name": "ordnance-survey-grid-reference",
                "revision_timestamp": "2010-03-19T17:59:21.466804",
                "state": "active",
                "id": "cce6c86f-c495-4109-843e-2a2a06c7feac"
            },
            {
                "vocabulary_id": null,
                "display_name": "osgr",
                "name": "osgr",
                "revision_timestamp": "2010-03-19T17:59:21.466804",
                "state": "active",
                "id": "f593ecb7-2763-4fd6-ab34-51533576ef5b"
            },
            {
                "vocabulary_id": null,
                "display_name": "plane",
                "name": "plane",
                "revision_timestamp": "2010-03-19T17:59:21.466804",
                "state": "active",
                "id": "b320ad6b-1203-4cee-8e62-cb861ae04253"
            },
            {
                "vocabulary_id": null,
                "display_name": "port",
                "name": "port",
                "revision_timestamp": "2010-03-19T17:59:21.466804",
                "state": "active",
                "id": "90b4514e-fa95-4d7d-a72a-117747d0f029"
            },
            {
                "vocabulary_id": null,
                "display_name": "public-transport",
                "name": "public-transport",
                "revision_timestamp": "2010-03-19T17:59:21.466804",
                "state": "active",
                "id": "479e7165-18fa-41b6-90be-74ecb6824e67"
            },
            {
                "vocabulary_id": null,
                "display_name": "rail",
                "name": "rail",
                "revision_timestamp": "2010-03-19T17:59:21.466804",
                "state": "active",
                "id": "1d94b03e-4356-4f7b-b82e-42bb012749be"
            },
            {
                "vocabulary_id": null,
                "display_name": "rail-station",
                "name": "rail-station",
                "revision_timestamp": "2010-03-19T17:59:21.466804",
                "state": "active",
                "id": "bbc2a4ed-e818-4fb2-bede-48ad07d830a1"
            },
            {
                "vocabulary_id": null,
                "display_name": "railway-station",
                "name": "railway-station",
                "revision_timestamp": "2010-03-19T17:59:21.466804",
                "state": "active",
                "id": "67ba321b-4124-4949-a4ed-6e55eb5cb0f2"
            },
            {
                "vocabulary_id": null,
                "display_name": "road",
                "name": "road",
                "revision_timestamp": "2010-03-19T17:59:21.466804",
                "state": "active",
                "id": "998a89fe-2a2b-441d-9515-5553e9681231"
            },
            {
                "vocabulary_id": null,
                "display_name": "station",
                "name": "station",
                "revision_timestamp": "2010-03-19T17:59:21.466804",
                "state": "active",
                "id": "f84b73b1-87c3-44d6-85f9-02e4ec020721"
            },
            {
                "vocabulary_id": null,
                "display_name": "stop",
                "name": "stop",
                "revision_timestamp": "2010-03-19T17:59:21.466804",
                "state": "active",
                "id": "8451e4b3-aea5-4a84-8ae9-2f25cb6bfcb3"
            },
            {
                "vocabulary_id": null,
                "display_name": "train",
                "name": "train",
                "revision_timestamp": "2010-03-19T17:59:21.466804",
                "state": "active",
                "id": "67d156c2-2d58-4a21-9b4c-4543d10b3c97"
            },
            {
                "vocabulary_id": null,
                "display_name": "tram",
                "name": "tram",
                "revision_timestamp": "2010-03-19T17:59:21.466804",
                "state": "active",
                "id": "b6c239f2-69be-4f34-a17f-c906b468abeb"
            },
            {
                "vocabulary_id": null,
                "display_name": "transport",
                "name": "transport",
                "revision_timestamp": "2010-03-19T17:59:21.466804",
                "state": "active",
                "id": "8b1aa1ca-ae20-4a88-8544-e7f7d432ef50"
            },
            {
                "vocabulary_id": null,
                "display_name": "transport-access",
                "name": "transport-access",
                "revision_timestamp": "2010-03-19T17:59:21.466804",
                "state": "active",
                "id": "0d504670-8bf6-4983-b07f-9c3ac6e4f1a0"
            },
            {
                "vocabulary_id": null,
                "display_name": "transport-access-node",
                "name": "transport-access-node",
                "revision_timestamp": "2010-03-19T17:59:21.466804",
                "state": "active",
                "id": "8f48c7cf-8337-4e3c-80c9-0877529448ce"
            },
            {
                "vocabulary_id": null,
                "display_name": "transport-interchange",
                "name": "transport-interchange",
                "revision_timestamp": "2010-03-19T17:59:21.466804",
                "state": "active",
                "id": "1f8d554e-fcfb-4840-ac9e-017e3d1c3765"
            },
            {
                "vocabulary_id": null,
                "display_name": "tube",
                "name": "tube",
                "revision_timestamp": "2010-03-19T17:59:21.466804",
                "state": "active",
                "id": "d9b72076-088d-4a2e-9859-f37ede88891f"
            },
            {
                "vocabulary_id": null,
                "display_name": "underground",
                "name": "underground",
                "revision_timestamp": "2010-03-19T17:59:21.466804",
                "state": "active",
                "id": "c8898db0-770a-4f6e-9226-14c50a19aaad"
            }
        ],
        "title": "National Public Transport Access Nodes (NaPTAN)",
        "foi-name": "",
        "precision": "+/- 1 metre spatial accuracy of Ordnance Survey Grid Reference",
        "tracking_summary": {
            "total": 0,
            "recent": 0
        },
        "contact-phone": "",
        "mandate": "",
        "relationships_as_subject": [ ],
        "groups": [ ],
        "num_tags": 32,
        "update_frequency-other": "weekly",
        "contact-name": "",
        "name": "naptan",
        "isopen": true,
        "url": "http://www.dft.gov.uk/naptan/ ",
        "type": "dataset",
        "notes": "NaPTAN is a GB national system for uniquely identifying all the points of access to public transport in GB. It is a core component of the GB national transport information infrastructure and is used by a number of other UK standards and information systems. Every GB station, coach terminus, airport, ferry terminal, bus stop, etc., is allocated at least one identifier.<br>\r\n<br>\r\nRelevant links:<br>\r\n<a href=\"http://www.dft.gov.uk/naptan/\">NaPTAN home page on DfT website (for background information)</a><br>\r\n<a href=\"http://data.gov.uk/dataset/nptg\">National Public Transport Gazetteer</a><br>\r\n<a href=\"http://data.gov.uk/dataset/nptdr\">National Public Transport Data Repository</a> (public transport timetables)<br>\r\n<a href=\"http://traveline.info/tnds.html\">Traveline National Data Set</a> (a weekly snapshot of public transport timetables due to be produced from early / mid 2012)\r\n",
        "owner_org": "72155ce7-f3b4-4211-9175-6c86703d7e6c",
        "extras": [
            {
                "package_id": "ff93ffc1-6656-47d8-9155-85ea0b8f2251",
                "value": "",
                "revision_timestamp": "2013-10-15T15:41:38.507351",
                "state": "active",
                "key": "contact-email",
                "revision_id": "c2ff5efc-1234-404d-8cd2-7e1c3c13fe62",
                "id": "8c11a846-9a77-4510-a21e-64e6a43ff89f"
            },
            {
                "package_id": "ff93ffc1-6656-47d8-9155-85ea0b8f2251",
                "value": "",
                "revision_timestamp": "2014-06-30T16:27:15.592599",
                "state": "active",
                "key": "contact-name",
                "revision_id": "68204f9c-0b15-4064-9c56-10b33ff63ee3",
                "id": "30590f70-12f7-4411-b109-e7309713bb5f"
            },
            {
                "package_id": "ff93ffc1-6656-47d8-9155-85ea0b8f2251",
                "value": "",
                "revision_timestamp": "2013-10-15T15:41:38.507351",
                "state": "active",
                "key": "contact-phone",
                "revision_id": "c2ff5efc-1234-404d-8cd2-7e1c3c13fe62",
                "id": "d7a3c5f1-a52b-4469-bd2a-eca6941a5c90"
            },
            {
                "package_id": "ff93ffc1-6656-47d8-9155-85ea0b8f2251",
                "value": "true",
                "revision_timestamp": "2013-10-30T21:41:55.592322",
                "state": "active",
                "key": "core-dataset",
                "revision_id": "0e19f2e9-82d7-4cb0-a0d3-1fc8fd776592",
                "id": "b712cc46-475e-42cb-91fd-73e3e471e564"
            },
            {
                "package_id": "ff93ffc1-6656-47d8-9155-85ea0b8f2251",
                "value": "2010-07-01",
                "revision_timestamp": "2010-08-11T15:39:18.086900",
                "state": "active",
                "key": "date_released",
                "revision_id": "94970c31-3fe4-440e-8e12-fd5592cca62e",
                "id": "fad41f81-58ab-485a-b723-8e9bc2814f06"
            },
            {
                "package_id": "ff93ffc1-6656-47d8-9155-85ea0b8f2251",
                "value": "2014-10-07",
                "revision_timestamp": "2014-10-07T14:19:20.083529",
                "state": "active",
                "key": "date_updated",
                "revision_id": "190baf69-3e83-437d-b8d1-e903d54d11b7",
                "id": "e07da5b9-5887-4b53-9fbd-c4a76d3e880b"
            },
            {
                "package_id": "ff93ffc1-6656-47d8-9155-85ea0b8f2251",
                "value": "",
                "revision_timestamp": "2013-10-15T15:41:38.507351",
                "state": "active",
                "key": "foi-email",
                "revision_id": "c2ff5efc-1234-404d-8cd2-7e1c3c13fe62",
                "id": "42ddd487-396f-4de3-92ea-a347f86593e5"
            },
            {
                "package_id": "ff93ffc1-6656-47d8-9155-85ea0b8f2251",
                "value": "",
                "revision_timestamp": "2013-10-15T15:41:38.507351",
                "state": "active",
                "key": "foi-name",
                "revision_id": "c2ff5efc-1234-404d-8cd2-7e1c3c13fe62",
                "id": "3020437e-79ff-4061-91a2-c2078c57744a"
            },
            {
                "package_id": "ff93ffc1-6656-47d8-9155-85ea0b8f2251",
                "value": "",
                "revision_timestamp": "2013-10-15T15:41:38.507351",
                "state": "active",
                "key": "foi-phone",
                "revision_id": "c2ff5efc-1234-404d-8cd2-7e1c3c13fe62",
                "id": "f1b02967-dbee-4d07-8efe-acf6513e17f0"
            },
            {
                "package_id": "ff93ffc1-6656-47d8-9155-85ea0b8f2251",
                "value": "",
                "revision_timestamp": "2013-02-26T14:29:09.213205",
                "state": "active",
                "key": "foi-web",
                "revision_id": "bdcecede-0df0-4391-a729-09c79657e2d4",
                "id": "4452a3ba-f8f8-4bc5-8ac3-3bed869f75b1"
            },
            {
                "package_id": "ff93ffc1-6656-47d8-9155-85ea0b8f2251",
                "value": "111000: Great Britain (England, Scotland, Wales)",
                "revision_timestamp": "2010-03-19T17:59:27.580127",
                "state": "active",
                "key": "geographic_coverage",
                "revision_id": "b4196d96-aa94-429a-8e81-2a432a3187d5",
                "id": "396304dc-e005-41f8-9324-d8adaec6b6cb"
            },
            {
                "package_id": "ff93ffc1-6656-47d8-9155-85ea0b8f2251",
                "value": "",
                "revision_timestamp": "2011-04-04T11:20:53.703085",
                "state": "active",
                "key": "mandate",
                "revision_id": "605ee56f-52d7-48d5-954c-e5f847aae32a",
                "id": "e79ae150-4e44-475f-823b-66322951cb85"
            },
            {
                "package_id": "ff93ffc1-6656-47d8-9155-85ea0b8f2251",
                "value": "+/- 1 metre spatial accuracy of Ordnance Survey Grid Reference",
                "revision_timestamp": "2010-03-19T17:59:27.580127",
                "state": "active",
                "key": "precision",
                "revision_id": "b4196d96-aa94-429a-8e81-2a432a3187d5",
                "id": "0f8a58d8-f55a-4e4c-aad7-780f610a3c22"
            },
            {
                "package_id": "ff93ffc1-6656-47d8-9155-85ea0b8f2251",
                "value": "2011-04-01",
                "revision_timestamp": "2011-04-04T11:20:53.703085",
                "state": "active",
                "key": "temporal_coverage-from",
                "revision_id": "605ee56f-52d7-48d5-954c-e5f847aae32a",
                "id": "b7a0ce25-1504-4f25-af5d-796e9f47fcec"
            },
            {
                "package_id": "ff93ffc1-6656-47d8-9155-85ea0b8f2251",
                "value": "2014-10-07",
                "revision_timestamp": "2014-10-07T14:18:55.719989",
                "state": "active",
                "key": "temporal_coverage-to",
                "revision_id": "3c82f37d-6844-4610-9daa-6f1d64caec60",
                "id": "0024b0c7-5355-4c2e-83c2-206d4550911f"
            },
            {
                "package_id": "ff93ffc1-6656-47d8-9155-85ea0b8f2251",
                "value": "day",
                "revision_timestamp": "2011-02-17T23:04:00.221881",
                "state": "active",
                "key": "temporal_granularity",
                "revision_id": "c6b70e68-e3df-4afb-b25b-22109f6a8f3c",
                "id": "4bd4fc85-3589-434f-afa5-e850e8115b06"
            },
            {
                "package_id": "ff93ffc1-6656-47d8-9155-85ea0b8f2251",
                "value": "Transport",
                "revision_timestamp": "2013-11-14T07:30:31.759264",
                "state": "active",
                "key": "theme-primary",
                "revision_id": "a60d9464-6d93-46cd-b37c-a16be434022a",
                "id": "97ed8db8-de37-45b6-a80a-f95b48308e23"
            },
            {
                "package_id": "ff93ffc1-6656-47d8-9155-85ea0b8f2251",
                "value": "false",
                "revision_timestamp": "2013-09-03T14:24:22.102692",
                "state": "active",
                "key": "unpublished",
                "revision_id": "ac6c2661-2e1a-46c7-95df-ee4ce5bc0195",
                "id": "f7e0de03-a396-47e7-a7d5-0440f369b4b6"
            },
            {
                "package_id": "ff93ffc1-6656-47d8-9155-85ea0b8f2251",
                "value": "weekly",
                "revision_timestamp": "2012-05-24T08:40:17.807689",
                "state": "active",
                "key": "update_frequency",
                "revision_id": "889f1687-bc95-488b-89e6-83510ed4f657",
                "id": "e19d06ad-8dca-4cb5-b838-7d9f76c205a3"
            }
        ],
        "license_url": "http://www.nationalarchives.gov.uk/doc/open-government-licence/version/2/",
        "individual_resources": [
            {
                "mimetype": "text/html",
                "cache_url": "http://data.gov.uk/data/resource_cache/f2/f2556c38-c68f-4288-aa58-91ef9eef46cb/resource",
                "hash": "257eac5eb8dc5fbb6893e611c6bca30b89895d78",
                "description": "NaPTAN home page on DfT website (for background information)",
                "format": "HTML",
                "url": "http://www.dft.gov.uk/naptan/",
                "cache_last_updated": "2013-06-19T04:36:54.403838",
                "cache_filepath": "/mnt/shared/ckan_resource_cache/f2/f2556c38-c68f-4288-aa58-91ef9eef46cb/resource",
                "tracking_summary": {
                    "total": 0,
                    "recent": 0
                },
                "last_modified": "2014-02-15T06:24:00.473683",
                "position": 0,
                "revision_id": "fb79b999-9721-4b93-8628-104ab0a6a687",
                "id": "f2556c38-c68f-4288-aa58-91ef9eef46cb",
                "resource_type": "file",
                "size": 12014
            },
            {
                "mimetype": "text/xml",
                "cache_url": "http://data.gov.uk/data/resource_cache/77/77d4437f-fc27-424f-a18c-e308b81475e7/NaPTAN-metadata.xml",
                "hash": "054da2c7e61e077077c81c9a981c1fd8e1df7a94",
                "description": "Meta-data",
                "format": "XML",
                "url": "http://www.dft.gov.uk/NaPTAN/snapshot/NaPTAN-metadata.xml",
                "cache_last_updated": "2013-06-19T19:47:22.977295",
                "cache_filepath": "/mnt/shared/ckan_resource_cache/77/77d4437f-fc27-424f-a18c-e308b81475e7/NaPTAN-metadata.xml",
                "tracking_summary": {
                    "total": 0,
                    "recent": 0
                },
                "last_modified": "2014-05-10T04:25:32.563970",
                "position": 1,
                "revision_id": "7d5e8e05-6e17-48a4-b879-e5b52dc8a4b7",
                "id": "77d4437f-fc27-424f-a18c-e308b81475e7",
                "resource_type": "file",
                "size": 3035
            },
            {
                "mimetype": "application/x-zip-compressed",
                "cache_url": "http://data.gov.uk/data/resource_cache/e3/e3d0c00c-abb7-4159-b512-5e3ac394780a/NaPTANcsv.zip",
                "hash": "1b6b5a06f43e016f5553ef16330ef943bbba0f19",
                "description": "Zipped CSV format",
                "format": "CSV",
                "url": "http://www.dft.gov.uk/NaPTAN/snapshot/NaPTANcsv.zip",
                "cache_last_updated": "2013-06-19T19:47:59.323345",
                "cache_filepath": "/mnt/shared/ckan_resource_cache/e3/e3d0c00c-abb7-4159-b512-5e3ac394780a/NaPTANcsv.zip",
                "tracking_summary": {
                    "total": 0,
                    "recent": 0
                },
                "last_modified": "2014-05-10T04:25:48.841828",
                "position": 2,
                "revision_id": "9b24e4a2-e1c8-4752-9779-b2f697880bd4",
                "id": "e3d0c00c-abb7-4159-b512-5e3ac394780a",
                "resource_type": "file",
                "size": 27658214
            },
            {
                "mimetype": "application/x-zip-compressed",
                "cache_url": "http://data.gov.uk/data/resource_cache/d6/d6dcb728-844b-45b9-a3cb-3db07dd50701/NaPTANxml.zip",
                "hash": "32f2fdb431755c07e204a92165a3c8a153556730",
                "description": "Zipped XML format",
                "format": "XML",
                "url": "http://www.dft.gov.uk/NaPTAN/snapshot/NaPTANxml.zip",
                "cache_last_updated": "2013-06-19T19:48:30.486601",
                "cache_filepath": "/mnt/shared/ckan_resource_cache/d6/d6dcb728-844b-45b9-a3cb-3db07dd50701/NaPTANxml.zip",
                "tracking_summary": {
                    "total": 0,
                    "recent": 0
                },
                "last_modified": "2014-05-10T04:25:51.133300",
                "position": 3,
                "revision_id": "c3ab6c95-e139-4406-b661-8a2f42444683",
                "id": "d6dcb728-844b-45b9-a3cb-3db07dd50701",
                "resource_type": "file",
                "size": 33440993
            },
            {
                "hash": "",
                "description": "GTFS format",
                "created": "2014-06-12T15:23:06.021769",
                "url": "http://www.dft.gov.uk/NaPTAN/snapshot/GTFS.zip",
                "format": "ZIP",
                "tracking_summary": {
                    "total": 0,
                    "recent": 0
                },
                "position": 4,
                "revision_id": "a64d7694-c07f-4f41-9fac-cdc3f7c097a2",
                "id": "88428c00-bf0f-46e9-8aec-434b0f9f5757",
                "resource_type": "file"
            }
        ],
        "update_frequency": "other",
        "revision_id": "33f3c21f-cf25-40b9-b2bb-b7ce631b402c",
        "date_released": "1/7/2010",
        "foi-phone": "",
        "theme-primary": "Transport"
    }

}
"""