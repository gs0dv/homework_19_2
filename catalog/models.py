from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    category_name = models.CharField(max_length=250, verbose_name='наименование')
    category_description = models.TextField(verbose_name='описание', **NULLABLE)
    # create_at = models.TextField(verbose_name='создано', **NULLABLE)

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    product_name = models.CharField(max_length=250, verbose_name='наименование')
    product_description = models.TextField(verbose_name='описание', **NULLABLE)
    preview_image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.FloatField(verbose_name='цена за покупку', **NULLABLE)
    date_create = models.DateField(**NULLABLE, verbose_name='дата создания')
    date_modify = models.DateField(**NULLABLE, verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.product_name} ({self.price})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
