# Generated by Django 5.1.6 on 2025-02-15 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_inventory_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='user',
        ),
    ]
