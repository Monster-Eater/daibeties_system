# Generated by Django 4.1.7 on 2023-04-12 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_insulin5_results_insulin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='Age',
            field=models.FloatField(max_length=100),
        ),
        migrations.AlterField(
            model_name='results',
            name='BMI',
            field=models.FloatField(max_length=100),
        ),
        migrations.AlterField(
            model_name='results',
            name='Blood_Pressure',
            field=models.FloatField(max_length=100),
        ),
        migrations.AlterField(
            model_name='results',
            name='D_P_Function',
            field=models.FloatField(max_length=100),
        ),
        migrations.AlterField(
            model_name='results',
            name='Glucose',
            field=models.FloatField(max_length=100),
        ),
        migrations.AlterField(
            model_name='results',
            name='Insulin',
            field=models.FloatField(max_length=100),
        ),
        migrations.AlterField(
            model_name='results',
            name='Pregnancies',
            field=models.FloatField(max_length=100),
        ),
        migrations.AlterField(
            model_name='results',
            name='Skin_Thickness',
            field=models.FloatField(max_length=100),
        ),
    ]