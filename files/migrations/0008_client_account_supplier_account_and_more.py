# Generated by Django 4.2.2 on 2023-07-01 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0011_alter_city_county_alter_company_economic_activity_and_more'),
        ('files', '0007_client_city_client_country_client_county_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clients_account', to='files.account'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='suppliers_account', to='files.account'),
        ),
        migrations.AlterField(
            model_name='account',
            name='account_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accounts_account_type', to='configurations.accounttype'),
        ),
    ]