# Generated by Django 3.2.7 on 2021-10-18 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_auto_20211017_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='students_model',
            name='stdnt_Gender',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teachers_model',
            name='tech_Gender',
            field=models.BooleanField(default=False),
        ),
    ]
