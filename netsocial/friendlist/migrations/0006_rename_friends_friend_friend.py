# Generated by Django 4.2.5 on 2023-09-10 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friendlist', '0005_rename_friend_friend_friends'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friend',
            old_name='friends',
            new_name='friend',
        ),
    ]
