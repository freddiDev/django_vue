# Generated by Django 4.2.16 on 2024-09-14 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='rating',
            new_name='price',
        ),
    ]
