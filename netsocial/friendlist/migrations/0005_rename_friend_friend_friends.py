# Generated by Django 4.2.5 on 2023-09-10 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friendlist', '0004_friendrequest_friend'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friend',
            old_name='friend',
            new_name='friends',
        ),
    ]
