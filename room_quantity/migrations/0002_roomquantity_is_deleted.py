# Generated by Django 4.1.13 on 2023-11-22 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room_quantity', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomquantity',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
