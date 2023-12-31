# Generated by Django 4.2.3 on 2023-07-21 20:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Company', '0006_alter_company_company_manager'),
        ('Employee', '0003_alter_employee_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('product_id', models.CharField(max_length=6)),
                ('available', models.BooleanField(default=True)),
                ('condition', models.CharField(choices=[('1', 'Good'), ('2', 'Average'), ('3', 'Bad')], default='1', max_length=1)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='device_company', to='Company.company')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkout_date', models.DateField()),
                ('checkin_date', models.DateField(blank=True, null=True)),
                ('condition_at_checkout_day', models.CharField(choices=[('1', 'Good'), ('2', 'Average'), ('3', 'Bad')], max_length=1)),
                ('condition_at_checkin_day', models.CharField(blank=True, choices=[('1', 'Good'), ('2', 'Average'), ('3', 'Bad')], max_length=1, null=True)),
                ('comment', models.TextField(max_length=512)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='device_log', to='Device.device')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_log', to='Employee.employee')),
            ],
        ),
    ]
