# Generated by Django 4.1.4 on 2022-12-22 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("equip", "0006_equipmenttype_equipment_equip_type"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="maintenance",
            options={
                "ordering": ("-updated_at",),
                "verbose_name_plural": "maintenance",
            },
        ),
        migrations.AlterField(
            model_name="equipmentmodel",
            name="computer_model",
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="equipmentmodel",
            name="make",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="makes",
                to="equip.make",
            ),
        ),
    ]