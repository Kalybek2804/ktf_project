# Generated by Django 3.2.7 on 2021-12-09 17:03

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=0, size=[1280, 958], upload_to='images'),
        ),
    ]
