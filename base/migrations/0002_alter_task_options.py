# Generated by Django 4.1.7 on 2023-06-15 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['complete'], 'verbose_name': 'Users'},
        ),
    ]