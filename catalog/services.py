from django.core.cache import cache
from .models import Product


def get_category_product(category_id):
    key = f"category_products_{category_id}"
    prods_list = cache.get(key)
    if prods_list is not None:
        return prods_list
    prods_list = Product.objects.filter(category_id=category_id)
    cache.set(key, prods_list, 60 * 15)
    return prods_list
