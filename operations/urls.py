from rest_framework import routers
from operations import views

app_name = 'operations'
router_product = routers.DefaultRouter()

# API endpoints operations:
# - cash and bank register
# - consumption receipts
router_product.register('cash-and-bank-register', views.CashAndBankRegisterViewset)
router_product.register('consumption-receipts', views.ConsumptionReceiptsViewset)

urlpatterns = router_product.urls