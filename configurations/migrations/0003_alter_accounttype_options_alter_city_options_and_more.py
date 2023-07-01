# Generated by Django 4.2.2 on 2023-06-28 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0002_city_company_country_county_currencycode_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accounttype',
            options={'verbose_name': 'Account types'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'Cities'},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Companies'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'Countries'},
        ),
        migrations.AlterModelOptions(
            name='county',
            options={'verbose_name': 'Counties'},
        ),
        migrations.AlterModelOptions(
            name='currencycode',
            options={'verbose_name': 'Currency codes'},
        ),
        migrations.AlterModelOptions(
            name='documenttype',
            options={'verbose_name': 'Document types'},
        ),
        migrations.AlterModelOptions(
            name='economicactivity',
            options={'verbose_name': 'Economic activities'},
        ),
        migrations.AlterModelOptions(
            name='producttype',
            options={'verbose_name': 'Product types'},
        ),
        migrations.AlterModelOptions(
            name='unitofmeasurement',
            options={'verbose_name': 'Unit of measurements'},
        ),
        migrations.AlterModelOptions(
            name='vattype',
            options={'verbose_name': 'Vat types'},
        ),
        migrations.AlterModelOptions(
            name='warehousetype',
            options={'verbose_name': 'Warehouse types'},
        ),
    ]
