# Generated by Django 4.0 on 2022-12-08 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('danceapp', '0023_trackinghistory_classname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trackinghistory',
            name='classname',
        ),
        migrations.AlterField(
            model_name='trackinghistory',
            name='payment',
            field=models.CharField(blank=True, default=0, max_length=200, null=True),
        ),
    ]