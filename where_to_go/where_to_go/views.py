import json
from django.shortcuts import render

from places.models import Location


def main(request):
    locations = Location.objects.all()

    features = []
    id_count = 1000
    latitude = 37.62
    longitude = 55.793676
    for location in locations:
        id_count += 1
        latitude += 0.02
        longitude -= 0.04
        features.append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [latitude, longitude]
                },
                "properties": {
                    "title": location.title,
                    "placeId": id_count,
                    "detailsUrl": "static/places/moscow_legends.json"
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
