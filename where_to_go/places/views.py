import json

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from places.models import Location


def places(request, place_id):
    place = get_object_or_404(Location, id=place_id)
    context = {'place': place}

    with open('where_to_go/static/places/locations.json', 'r') as ff:
        file = json.load(ff)
    for location in file:
        if location['title'] == place.title:
            context = location
            break
    return JsonResponse(context, json_dumps_params={'indent': 2, 'ensure_ascii': False})
