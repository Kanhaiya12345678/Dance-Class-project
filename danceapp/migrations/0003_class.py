# Generated by Django 4.0 on 2022-11-26 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('danceapp', '0002_remove_registration_user_registration_gender_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classname', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('cost', models.CharField(blank=True, max_length=200, null=True)),
                ('creationdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
