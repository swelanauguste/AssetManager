# Generated by Django 4.1.4 on 2022-12-22 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("equip", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="computer",
            name="location",
            field=models.TextField(blank=True),
        ),
    ]
