# Generated by Django 4.1.2 on 2022-10-22 13:36

from django.db import migrations
from django.db import transaction


def create_connection_flat_with_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    flats = Flat.objects.all().iterator()
    for flat in flats:
        with transaction.atomic():
            flat.flats_by.get_or_create(owner=flat.owner)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20221022_1514'),
    ]

    operations = [
        migrations.RunPython(create_connection_flat_with_owners)
    ]
