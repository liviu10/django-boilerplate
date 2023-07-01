from rest_framework import routers
from operations import views

app_name = 'operations'
router_product = routers.DefaultRouter()

# API endpoints operations:
# - cash and bank register
# - invoices
# - consumption receipts
# - invoice lines
# - consumption receipts lines
# - sales invoice
# - shipping notes
# - sales invoice lines
# - shipping note lines
router_product.register('cash-and-bank-register', views.CashAndBankRegisterViewset)
router_product.register('invoices', views.InvoicesViewset)
router_product.register('consumption-receipts', views.ConsumptionReceiptsViewset)
router_product.register('invoice-lines', views.InvoiceLinesViewset)
router_product.register('consumption-receipt-lines', views.ConsumptionReceiptLinesViewset)
router_product.register('sales-invoices', views.SalesInvoicesViewset)
router_product.register('shipping-notes', views.ShippingNotesViewset)
router_product.register('sales-invoice-lines', views.SalesInvoiceLinesViewset)
router_product.register('shipping-note-lines', views.ShippingNoteLinesViewset)

urlpatterns = router_product.urls