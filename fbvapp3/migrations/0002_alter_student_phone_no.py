# Generated by Django 5.0.4 on 2024-04-28 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbvapp3', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone_no',
            field=models.IntegerField(),
        ),
    ]
