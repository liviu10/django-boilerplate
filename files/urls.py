from rest_framework import routers
from files import views

app_name = 'files'
router_product = routers.DefaultRouter()

# API endpoints files:
# - accounts
# - clients
# - products
# - suppliers
router_product.register('accounts', views.AccountsViewset)
router_product.register('clients', views.ClientsViewset)
router_product.register('products', views.ProductsViewset)
router_product.register('suppliers', views.SuppliersViewset)

urlpatterns = router_product.urls