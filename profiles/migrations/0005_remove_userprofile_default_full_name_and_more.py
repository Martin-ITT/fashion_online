# Generated by Django 4.1.7 on 2023-08-24 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_rename_full_name_userprofile_default_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='default_full_name',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]