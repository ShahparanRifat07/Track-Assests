# Generated by Django 4.2.3 on 2023-07-20 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Employee', '0001_initial'),
        ('Company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_manager',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Employee.employee'),
        ),
    ]
