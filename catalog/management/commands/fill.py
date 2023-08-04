from django.core.management import BaseCommand
from catalog.models import Category, Product

from django.core.management.color import no_style
from django.db import connection


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        sequence_sql = connection.ops.sequence_reset_sql(no_style(), [Category, Product])
        with connection.cursor() as cursor:
            for sql in sequence_sql:
                cursor.execute(sql)

        category_list = [
            {'category_name': 'Овощи'},
            {'category_name': 'Фрукты'},
            {'category_name': 'Ягоды'}
        ]

        product_list = [
            {'product_name': 'Огурцы', 'category_id': '1', 'price': 100},
            {'product_name': 'Яблоки', 'category_id': '2', 'price': 200},
            {'product_name': 'Малина', 'category_id': '3', 'price': 300},
            {'product_name': 'Помидоры', 'category_id': '1', 'price': 150},
        ]

        products_for_create = []

        for category_item in category_list:
            Category.objects.create(**category_item)

        for product_item in product_list:
            products_for_create.append(Product(**product_item))
        Product.objects.bulk_create(products_for_create)
