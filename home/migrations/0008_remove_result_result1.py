# Generated by Django 4.1.7 on 2023-04-12 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='result1',
        ),
    ]
