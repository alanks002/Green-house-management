# Generated by Django 5.0.1 on 2024-02-16 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_statedb_remove_singledb_city_remove_singledb_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='singledb',
            name='State',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
