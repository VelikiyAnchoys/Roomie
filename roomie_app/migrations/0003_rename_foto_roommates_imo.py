# Generated by Django 5.1.3 on 2024-11-30 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roomie_app', '0002_ad_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roommates',
            old_name='foto',
            new_name='imo',
        ),
    ]