# Generated by Django 5.0.7 on 2024-10-14 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.BigIntegerField(),
        ),
    ]