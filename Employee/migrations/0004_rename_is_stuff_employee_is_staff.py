# Generated by Django 4.2.3 on 2023-07-22 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0003_alter_employee_updated_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='is_stuff',
            new_name='is_staff',
        ),
    ]