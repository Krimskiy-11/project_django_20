from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **kwargs):

        group, _ = Category.objects.get_or_create(category_name='Смартфоны')

        products = [
            {'product_name': 'IPhone 12', 'price': '100000', 'category': group},
            {'product_name': 'Samsung S21','price': '120000', 'category': group},
            {'product_name': 'Pixel 5', 'price': '110000', 'category': group},
        ]

        for products_data in products:
            product, created = Product.objects.get_or_create(**products_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added student: {product.product_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Student already exists: {product.product_name}'))
