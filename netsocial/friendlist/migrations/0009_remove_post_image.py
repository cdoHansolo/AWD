# Generated by Django 4.2.5 on 2023-09-12 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friendlist', '0008_alter_friend_status_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]