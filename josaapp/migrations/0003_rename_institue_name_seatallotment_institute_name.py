# Generated by Django 4.2.1 on 2023-06-19 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('josaapp', '0002_seatallotment_institue_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seatallotment',
            old_name='Institue_name',
            new_name='Institute_name',
        ),
    ]
