# Generated by Django 4.1.7 on 2023-04-12 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_val1_results_age_rename_val2_results_bmi_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='results',
            old_name='Insulin5',
            new_name='Insulin',
        ),
    ]
