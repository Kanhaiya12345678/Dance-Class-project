# Generated by Django 4.0 on 2022-12-01 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('danceapp', '0013_registration_monthyear_registration_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='monthyear',
            new_name='payment',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='year',
        ),
    ]
