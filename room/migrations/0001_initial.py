# Generated by Django 4.1.13 on 2023-11-23 01:28

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('room_quantity', '0003_alter_roomquantity_quantity'),
        ('room_type', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='uploads/')),
                ('description', models.TextField()),
                ('star', models.CharField(blank=True, max_length=255, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('room_quantity', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='room_quantity.roomquantity')),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='room_type.roomtype')),
            ],
        ),
    ]
