# Generated by Django 4.2.2 on 2023-06-28 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('siruta_code', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('longitude', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('latitude', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('google_maps_url', models.CharField(blank=True, default='', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, unique=True)),
                ('fiscal_code', models.CharField(blank=True, default='', max_length=255, unique=True)),
                ('registration_number', models.CharField(blank=True, default='', max_length=255, null=True, unique=True)),
                ('social_capital', models.DecimalField(blank=True, decimal_places=4, max_digits=18)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CurrencyCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('code', models.CharField(blank=True, default='', max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, default='', max_length=3, unique=True)),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EconomicActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, default='', max_length=5, unique=True)),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UnitOfMeasurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, default='', max_length=5, unique=True)),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VatType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, default='', max_length=6, unique=True)),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('value', models.IntegerField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WarehouseType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, default='', max_length=3, unique=True)),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('type', models.IntegerField(blank=True, default='', max_length=255, null=True)),
            ],
        ),
    ]