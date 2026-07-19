from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (
    CategoryListView,
    ContactsView,
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    CategoryCreateView,
    CategoryUpdateView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", CategoryListView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),

    path("products_list/", ProductListView.as_view(), name="product_list"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product/new/", ProductCreateView.as_view(), name="product_create"),
    path("product/<int:pk>/edit/", ProductUpdateView.as_view(), name="product_update"),

    path("category/new/", CategoryCreateView.as_view(), name="category_create"),
    path("category/<int:pk>/edit", CategoryUpdateView.as_view(), name="category_update"),
]
