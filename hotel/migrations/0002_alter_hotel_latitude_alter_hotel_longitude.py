# Generated by Django 4.1.13 on 2023-11-22 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='latitude',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='longitude',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
