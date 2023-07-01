from rest_framework import routers
from configurations import views

app_name = 'configurations'
router_product = routers.DefaultRouter()

# API endpoints configurations:
# - account type
# - countries
# - counties
# - cities
# - currency codes
# - document types
# - economic activities
# - companies
# - company details
# - company settings
# - product types
# - unit of measurement
# - vat type
# - warehouse type
router_product.register('account-types', views.AccountTypesViewset)
router_product.register('countries', views.CountriesViewset)
router_product.register('counties', views.CountiesViewset)
router_product.register('cities', views.CitiesViewset)
router_product.register('currency-codes', views.CurrencyCodesViewset)
router_product.register('document-types', views.DocumentTypesViewset)
router_product.register('economic-activities', views.EconomicActivitiesViewset)
router_product.register('companies', views.CompaniesViewset)
router_product.register('company-details', views.CompanyDetailsViewset)
router_product.register('company-settings', views.CompanySettingsViewset)
router_product.register('product-types', views.ProductTypesViewset)
router_product.register('unit-of-measurement', views.UnitOfMeasurementsViewset)
router_product.register('vat-types', views.VatTypesViewset)
router_product.register('warehouse-types', views.WarehouseTypesViewset)

urlpatterns = router_product.urls