from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import CategoryListView, ContactsView, ProductListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('products_list/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail')
]
