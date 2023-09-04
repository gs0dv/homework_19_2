from django.conf import settings
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

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец')

    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.product_name} ({self.price})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        permissions = [
            (
                'set_published',
                'Can publish products'
            )
        ]


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.IntegerField(default=0, verbose_name='номер версии')
    version_name = models.CharField(max_length=150, verbose_name='название версии', **NULLABLE)
    is_current_version = models.BooleanField(default=True, verbose_name='признак текущей версии')

    def __str__(self):
        return f'{self.version_number} ({self.version_name})'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
