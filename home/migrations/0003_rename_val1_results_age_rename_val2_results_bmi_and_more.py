# Generated by Django 4.1.7 on 2023-04-12 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_results'),
    ]

    operations = [
        migrations.RenameField(
            model_name='results',
            old_name='val1',
            new_name='Age',
        ),
        migrations.RenameField(
            model_name='results',
            old_name='val2',
            new_name='BMI',
        ),
        migrations.RenameField(
            model_name='results',
            old_name='val3',
            new_name='Blood_Pressure',
        ),
        migrations.RenameField(
            model_name='results',
            old_name='val4',
            new_name='D_P_Function',
        ),
        migrations.RenameField(
            model_name='results',
            old_name='val5',
            new_name='Glucose',
        ),
        migrations.RenameField(
            model_name='results',
            old_name='val6',
            new_name='Insulin5',
        ),
        migrations.RenameField(
            model_name='results',
            old_name='val7',
            new_name='Pregnancies',
        ),
        migrations.RenameField(
            model_name='results',
            old_name='val8',
            new_name='Skin_Thickness',
        ),
    ]