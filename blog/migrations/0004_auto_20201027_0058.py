# Generated by Django 3.1.1 on 2020-10-26 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201027_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donate',
            name='fname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='donate',
            name='lname',
            field=models.CharField(default='', max_length=50),
        ),
    ]
