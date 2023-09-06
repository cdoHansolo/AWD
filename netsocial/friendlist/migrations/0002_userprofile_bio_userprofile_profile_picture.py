# Generated by Django 4.2.5 on 2023-09-06 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friendlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, max_length=400),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
    ]
