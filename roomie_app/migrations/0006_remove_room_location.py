# Generated by Django 5.1.3 on 2024-11-30 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roomie_app', '0005_alter_post_options_alter_room_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='location',
        ),
    ]