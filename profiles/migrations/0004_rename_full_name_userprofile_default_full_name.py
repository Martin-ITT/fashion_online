# Generated by Django 4.1.7 on 2023-08-24 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_userprofile_full_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='full_name',
            new_name='default_full_name',
        ),
    ]
