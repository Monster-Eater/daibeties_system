# Generated by Django 4.1.7 on 2023-04-13 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_reports_age_alter_reports_bmi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reports',
            name='user',
            field=models.CharField(max_length=50, verbose_name='User Name'),
        ),
    ]
