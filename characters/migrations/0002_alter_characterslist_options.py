# Generated by Django 4.2.3 on 2023-07-31 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='characterslist',
            options={'verbose_name': 'Character List', 'verbose_name_plural': 'Characters List'},
        ),
    ]
