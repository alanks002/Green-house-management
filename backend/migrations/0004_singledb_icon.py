# Generated by Django 5.0.1 on 2024-02-03 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_delete_prodb'),
    ]

    operations = [
        migrations.AddField(
            model_name='singledb',
            name='Icon',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
