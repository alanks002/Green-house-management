# Generated by Django 5.0.1 on 2024-02-23 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_bookingdb_total_alter_bookingdb_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingdb',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bookingdb',
            name='razor_payment_id',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
