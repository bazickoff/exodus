# Generated by Django 2.2.9 on 2020-02-08 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0002_auto_20180420_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracker',
            name='apps_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tracker',
            name='apps_percent',
            field=models.IntegerField(default=0),
        ),
    ]
