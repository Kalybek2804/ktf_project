# Generated by Django 3.2.7 on 2021-12-10 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_rename_creat_at_new_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
