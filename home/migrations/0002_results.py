# Generated by Django 4.1.7 on 2023-04-12 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('val1', models.CharField(max_length=100)),
                ('val2', models.CharField(max_length=100)),
                ('val3', models.CharField(max_length=100)),
                ('val4', models.CharField(max_length=100)),
                ('val5', models.CharField(max_length=100)),
                ('val6', models.CharField(max_length=100)),
                ('val7', models.CharField(max_length=100)),
                ('val8', models.CharField(max_length=100)),
            ],
        ),
    ]
