# Generated by Django 4.2.5 on 2023-10-08 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sketchs', '0003_sketch_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sketch',
            name='slug',
        ),
    ]