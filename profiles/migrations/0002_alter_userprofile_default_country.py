# Generated by Django 4.1.7 on 2023-08-20 20:36

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='default_country',
            field=django_countries.fields.CountryField(blank=True, default='IE', max_length=2, null=True),
        ),
    ]
