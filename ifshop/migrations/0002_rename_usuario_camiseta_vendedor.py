# Generated by Django 5.1.3 on 2024-12-19 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ifshop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='camiseta',
            old_name='usuario',
            new_name='vendedor',
        ),
    ]
