# Generated by Django 3.2.7 on 2021-12-10 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_alter_new_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='news_view',
            field=models.IntegerField(default=0),
        ),
    ]