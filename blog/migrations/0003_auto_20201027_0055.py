# Generated by Django 3.1.1 on 2020-10-26 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_donate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donate',
            old_name='first_name',
            new_name='fname',
        ),
        migrations.RenameField(
            model_name='donate',
            old_name='last_name',
            new_name='lname',
        ),
    ]
