# Generated by Django 4.0 on 2022-11-28 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('danceapp', '0006_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pagetitle', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
