# Generated by Django 4.2.4 on 2023-08-30 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prediction_database', '0005_input_input_max_power'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='input',
            name='input_km_driven',
        ),
    ]
