# Generated by Django 5.0.1 on 2024-02-24 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0007_remove_bookingdb_paid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingdb',
            name='razorpay_order_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
