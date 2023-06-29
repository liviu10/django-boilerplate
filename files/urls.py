from rest_framework import routers
from files import views

app_name = 'files'
router_product = routers.DefaultRouter()

# API endpoints files:
# - accounts
router_product.register('accounts', views.AccountsViewset)

urlpatterns = router_product.urls