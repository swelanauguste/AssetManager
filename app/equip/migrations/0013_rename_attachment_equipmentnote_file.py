# Generated by Django 4.1.4 on 2022-12-24 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("equip", "0012_alter_equipmentnote_attachment"),
    ]

    operations = [
        migrations.RenameField(
            model_name="equipmentnote",
            old_name="attachment",
            new_name="file",
        ),
    ]