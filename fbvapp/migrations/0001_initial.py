# Generated by Django 5.0.4 on 2024-04-26 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('auther', models.CharField(max_length=40)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField(default=0)),
                ('duration', models.FloatField()),
            ],
        ),
    ]
