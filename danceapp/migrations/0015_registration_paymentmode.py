# Generated by Django 4.0 on 2022-12-01 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('danceapp', '0014_rename_monthyear_registration_payment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='paymentmode',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]