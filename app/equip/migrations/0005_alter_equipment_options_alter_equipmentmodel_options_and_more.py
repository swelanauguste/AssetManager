# Generated by Django 4.1.4 on 2022-12-22 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("equip", "0004_rename_computer_equipment_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="equipment",
            options={"ordering": ("-created_at",), "verbose_name_plural": "equipment"},
        ),
        migrations.AlterModelOptions(
            name="equipmentmodel",
            options={"ordering": ("computer_model",)},
        ),
        migrations.AlterModelOptions(
            name="make",
            options={"ordering": ("make",)},
        ),
        migrations.AlterModelOptions(
            name="status",
            options={"ordering": ("status",), "verbose_name_plural": "statuses"},
        ),
    ]
