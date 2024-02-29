# Generated by Django 5.0.1 on 2024-02-19 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=20, null=True)),
                ('Email', models.EmailField(blank=True, max_length=20, null=True)),
                ('Place', models.CharField(blank=True, max_length=20, null=True)),
                ('Message', models.CharField(blank=True, max_length=400, null=True)),
            ],
        ),
    ]