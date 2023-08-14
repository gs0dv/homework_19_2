from django.db import models

NULLABLE = {
    'blank': True,
    'null': True
}


class Blog(models.Model):
    header = models.CharField(max_length=250, verbose_name='заголовок')
    slug = models.CharField(max_length=250, verbose_name='slug', **NULLABLE)
    body = models.TextField(verbose_name='содержимое')
    preview_image = models.ImageField(upload_to='blogs/', verbose_name='превью(изображение)', **NULLABLE)
    date_create = models.DateField(verbose_name='дата создания', **NULLABLE)
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
