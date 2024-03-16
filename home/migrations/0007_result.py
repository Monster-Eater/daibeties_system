# Generated by Django 4.1.7 on 2023-04-12 09:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0006_delete_results'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pregnancies', models.FloatField(max_length=20)),
                ('Glucose', models.FloatField(max_length=20)),
                ('Blood_Pressure', models.FloatField(max_length=20)),
                ('Skin_Thickness', models.FloatField(max_length=20)),
                ('Insulin', models.FloatField(max_length=20)),
                ('BMI', models.FloatField(max_length=20)),
                ('D_P_Function', models.FloatField(max_length=20)),
                ('Age', models.FloatField(max_length=20)),
                ('result1', models.CharField(max_length=30)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
