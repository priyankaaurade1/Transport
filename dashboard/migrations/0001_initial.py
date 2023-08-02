# Generated by Django 4.2.3 on 2023-07-29 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_name', models.CharField(max_length=100)),
                ('driver_license_number', models.CharField(max_length=20)),
                ('driver_contact_number', models.CharField(max_length=15)),
                ('driver_address', models.CharField(max_length=15)),
            ],
        ),
    ]
