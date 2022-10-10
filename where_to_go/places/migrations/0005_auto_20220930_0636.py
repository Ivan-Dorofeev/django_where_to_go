# Generated by Django 4.1.1 on 2022-09-30 06:36
import json
import os
from pathlib import Path

from django.db import migrations


def img_from_json_to_model(apps, schema_editor):
    location_model = apps.get_model('places', 'Location')
    img_model = apps.get_model('places', 'Image')

    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    msk_legend_path = os.path.join(BASE_DIR, 'where_to_go/static/places/moscow_legends.json')
    roofs24_path = os.path.join(BASE_DIR, 'where_to_go/static/places/roofs24.json')

    with open(msk_legend_path, 'r') as file:
        msc_legends_file = json.load(file)
    msc_legends_imgs = msc_legends_file['imgs']
    msc_legends_title = msc_legends_file['title']

    with open(roofs24_path, 'r') as file:
        roofs24_file = json.load(file)
    roofs24_imgs = roofs24_file['imgs']
    roofs24_title = roofs24_file['title']

    for location in location_model.objects.all():
        if location.title == msc_legends_title:
            for img in msc_legends_imgs:
                img_model.objects.get_or_create(
                    location=location,
                    images=img)
        elif location.title == roofs24_title:
            for img in roofs24_imgs:
                img_model.objects.get_or_create(
                    location=location,
                    images=img)


class Migration(migrations.Migration):
    dependencies = [
        ('places', '0004_image_location_alter_image_images'),
    ]

    operations = [
        migrations.RunPython(img_from_json_to_model)
    ]
