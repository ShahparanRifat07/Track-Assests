# Generated by Django 4.2.3 on 2023-07-22 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0007_company_stripe_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='premium',
            field=models.BooleanField(default=False),
        ),
    ]
