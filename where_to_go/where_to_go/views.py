from django.shortcuts import render
from places.models import Location, Image


def main(request):
    locations = Location.objects.all()

    features = []
    id_count = 1000
    for location in locations:
        id_count += 1

        images = Image.objects.filter(location=location)
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
