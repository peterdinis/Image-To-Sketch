# Generated by Django 4.2.5 on 2023-10-01 15:10

from django.db import migrations, models
import sketchs.models


class Migration(migrations.Migration):

    dependencies = [
        ('sketchs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sketch',
            name='upload',
            field=models.ImageField(default='', upload_to=sketchs.models.user_directory_path),
        ),
    ]