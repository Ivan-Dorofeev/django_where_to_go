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
            img_count = 0
            for img in msc_legends_imgs:
                img_count += 1
                img_model.objects.get_or_create(
                    location=location,
                    images=f'{img_count} - {img}')
        elif location.title == roofs24_title:
            img_count = 0
            for img in roofs24_imgs:
                img_count += 1
                img_model.objects.get_or_create(
                    location=location,
                    images=f'{img_count} - {img}')


class Migration(migrations.Migration):
    dependencies = [
        ('places', '0005_auto_20220930_0636'),
    ]

    operations = [
        migrations.RunPython(img_from_json_to_model)
    ]
