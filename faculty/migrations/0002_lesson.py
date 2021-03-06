# Generated by Django 4.0 on 2021-12-18 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('lessons_name', models.CharField(max_length=255)),
                ('lesson_pdf', models.FileField(upload_to='')),
                ('lesson_teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lesson_teacher', to='faculty.teacher')),
            ],
        ),
    ]
