# Generated by Django 4.1.7 on 2023-04-13 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_result_delete_reports'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='result',
            new_name='Reports',
        ),
    ]
