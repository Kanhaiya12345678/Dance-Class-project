# Generated by Django 4.0 on 2022-12-01 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('danceapp', '0012_trackinghistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='monthyear',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='year',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
