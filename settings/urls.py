from rest_framework import routers
from settings import views

app_name = 'settings'
router_product = routers.DefaultRouter()

# API endpoints settings: accepted domains
router_product.register('accepted-domains', views.AcceptedDomainsViewset)

urlpatterns = router_product.urls