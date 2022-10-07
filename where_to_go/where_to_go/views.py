import json
from pprint import pprint

from django.shortcuts import render
from django.urls import reverse

from places.models import Location

from places.models import Image


def main(request):
    locations = Location.objects.all()
    images = Image.objects.all()

    features = []
    id_count = 1000
    for location in locations:
        id_count += 1
        imgs = [img.image.url for img in images]

        features.append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [location.latitude, location.longtitude]
                },
                "properties": {
                    "title": location.title,
                    "placeId": id_count,
                    "detailsUrl": {
                        "title": location.title,
                        "imgs": imgs,
                        "description_short": location.description,
                        "description_long": location.text,
                        "coordinates": {
                            "lng": location.longtitude,
                            "lat": location.latitude
                        }
                    }
                }
            }
        )
    context = {
        'geo_data': {
            "type": "FeatureCollection",
            "features": features
        }
    }
    return render(request, 'index.html', context)
