# Generated by Django 4.1.4 on 2022-12-24 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("equip", "0013_rename_attachment_equipmentnote_file"),
    ]

    operations = [
        migrations.RenameField(
            model_name="equipmentnote",
            old_name="file",
            new_name="attachment",
        ),
    ]