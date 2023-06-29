# Generated by Django 4.2.2 on 2023-06-28 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_accounttype_alter_accepteddomain_domain_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AccountType',
        ),
        migrations.AlterModelOptions(
            name='accepteddomain',
            options={'verbose_name': 'Accepted domains'},
        ),
        migrations.AlterModelOptions(
            name='errorandnotification',
            options={'verbose_name': 'Errors and notifications'},
        ),
    ]