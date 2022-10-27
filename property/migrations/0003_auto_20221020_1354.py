# Generated by Django 2.2.24 on 2022-10-20 10:54

from django.db import migrations


def is_flat_in_new_building(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        if flat.construction_year >= 2015:
            flat.new_building = True
        else:
            flat.new_building = False
        flat.save()            

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_auto_20221020_1240'),
    ]

    operations = [
        migrations.RunPython(is_flat_in_new_building),
    ]
