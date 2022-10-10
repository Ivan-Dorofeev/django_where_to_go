# Generated by Django 4.1.1 on 2022-09-30 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='location',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='location',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Название места'),
        ),
    ]