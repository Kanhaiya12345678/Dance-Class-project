# Generated by Django 4.0 on 2022-11-28 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('danceapp', '0009_registration_classname_registration_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='message',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
