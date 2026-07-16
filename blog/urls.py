from django.urls import path
from catalog.apps import CatalogConfig
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_list"),
    path("blogs/<int:pk>", BlogDetailView.as_view(), name="blog_detail"),
    path("blogs/new", BlogCreateView.as_view(), name="blog_create"),
    path("blogs/<int:pk>/edit", BlogUpdateView.as_view(), name="blog_edit"),
    path("blogs/<int:pk>/delete", BlogDeleteView.as_view(), name="blog_delete"),
]
