# Generated by Django 3.1.1 on 2020-10-26 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='donate',
            fields=[
                ('donate_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=70)),
                ('address', models.CharField(default='', max_length=70)),
                ('country', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
