# Generated by Django 4.0 on 2022-12-09 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('danceapp', '0025_remove_trackinghistory_payment_and_more'),
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
            field=models.CharField(blank=True, default=0, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='trackinghistory',
            name='paymentmode',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
