# Generated by Django 4.2.3 on 2023-07-21 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Device', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
