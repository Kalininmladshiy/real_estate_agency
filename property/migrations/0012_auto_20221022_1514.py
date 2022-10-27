# Generated by Django 4.1.2 on 2022-10-22 12:14

from django.db import migrations

def copy_customers_to_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    flats = Flat.objects.all().iterator()
    for flat in flats:
        Owner.objects.get_or_create(
            owner=flat.owner, 
            owners_phonenumber=flat.owners_phonenumber,
            owner_pure_phone=flat.owner_pure_phone,
        )


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_owner'),
    ]

    operations = [
        migrations.RunPython(copy_customers_to_owners),
    ]
