# Generated by Django 4.0 on 2022-12-06 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('danceapp', '0019_trackinghistory_classname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trackinghistory',
            name='classname',
        ),
    ]