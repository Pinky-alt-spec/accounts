# Generated by Django 2.1.7 on 2021-10-10 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userAccount', '0003_auto_20211010_1743'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='name',
            new_name='tasks',
        ),
    ]
