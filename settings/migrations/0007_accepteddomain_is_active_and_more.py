# Generated by Django 4.2.2 on 2023-07-01 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0006_accepteddomain_added_by_accepteddomain_created_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='accepteddomain',
            name='is_active',
            field=models.BooleanField(blank=True, choices=[(False, 'No'), (True, 'Yes')], default=False, null=True),
        ),
        migrations.AddField(
            model_name='errorandnotification',
            name='is_active',
            field=models.BooleanField(blank=True, choices=[(False, 'No'), (True, 'Yes')], default=False, null=True),
        ),
    ]
