# Generated by Django 3.2.7 on 2021-12-10 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_new_creat_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new',
            old_name='creat_at',
            new_name='create_date',
        ),
    ]