# Generated by Django 4.1.3 on 2022-11-27 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("partaker", "0003_remove_partaker_event_manager_partaker_event"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Manager",
        ),
    ]
