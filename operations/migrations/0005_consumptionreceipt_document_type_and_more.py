# Generated by Django 4.2.2 on 2023-07-01 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0010_companydetails_city_companydetails_country_and_more'),
        ('operations', '0004_cashandbankregister_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumptionreceipt',
            name='document_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='consumption_receipts', to='configurations.documenttype'),
        ),
        migrations.AddField(
            model_name='consumptionreceiptline',
            name='vat_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='consumption_receipt_lines_vat_type', to='configurations.vattype'),
        ),
        migrations.AddField(
            model_name='consumptionreceiptline',
            name='warehouse_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='consumption_receipt_lines_warehouse_type', to='configurations.warehousetype'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='document_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoices_document_type', to='configurations.documenttype'),
        ),
        migrations.AddField(
            model_name='invoiceline',
            name='product_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoice_lines_product_type', to='configurations.producttype'),
        ),
        migrations.AddField(
            model_name='invoiceline',
            name='unit_of_measurement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoice_lines_unit_of_measurement', to='configurations.unitofmeasurement'),
        ),
        migrations.AddField(
            model_name='invoiceline',
            name='vat_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoice_lines_vat_type', to='configurations.vattype'),
        ),
        migrations.AddField(
            model_name='invoiceline',
            name='warehouse_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoice_lines_warehouse_type', to='configurations.warehousetype'),
        ),
        migrations.AddField(
            model_name='salesinvoice',
            name='document_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sales_invoices', to='configurations.documenttype'),
        ),
        migrations.AddField(
            model_name='salesinvoiceline',
            name='product_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sales_invoice_lines_product_type', to='configurations.producttype'),
        ),
        migrations.AddField(
            model_name='salesinvoiceline',
            name='unit_of_measurement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sales_invoice_lines_unit_of_measurement', to='configurations.unitofmeasurement'),
        ),
        migrations.AddField(
            model_name='salesinvoiceline',
            name='vat_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sales_invoice_lines_vat_type', to='configurations.vattype'),
        ),
        migrations.AddField(
            model_name='salesinvoiceline',
            name='warehouse_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sales_invoice_lines_warehouse_type', to='configurations.warehousetype'),
        ),
        migrations.AddField(
            model_name='shippingnote',
            name='document_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shipping_notes', to='configurations.documenttype'),
        ),
        migrations.AddField(
            model_name='shippingnoteline',
            name='vat_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shipping_note_lines_vat_type', to='configurations.vattype'),
        ),
        migrations.AddField(
            model_name='shippingnoteline',
            name='warehouse_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shipping_note_lines_warehouse_type', to='configurations.warehousetype'),
        ),
    ]
