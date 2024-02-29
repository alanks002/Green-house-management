# Generated by Django 5.0.1 on 2024-02-23 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_service_bookingdb_city_bookingdb_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingdb',
            name='total',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bookingdb',
            name='state',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]