import json
from django.shortcuts import render

from places.models import Location


def main(request):
    locations = Location.objects.all()
    print('******* locations = ', locations)

    features = []
    id_count = 1000
    for location in locations:
        id_count += 1
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
                    "detailsUrl": ""
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
