# Generated by Django 4.0 on 2022-12-01 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('danceapp', '0015_registration_paymentmode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='paymentmode',
        ),
        migrations.AddField(
            model_name='trackinghistory',
            name='payment',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='trackinghistory',
            name='paymentmode',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
