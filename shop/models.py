from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    class MPTTMeta:
        order_insertion_by = ['name']
        verbose_name = 'Категория(ю)'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    seller = models.ForeignKey(
        User, related_name="user_product", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255, verbose_name='Название')
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, blank=True, verbose_name='Количество')
    unit = models.CharField(max_length=255, blank=True, null=True, verbose_name='Единица измерения')
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True, verbose_name='Изоброжение')
    time_create = models.DateField(auto_now_add=True, verbose_name='Дата')
    description = models.TextField(blank=True, null=True, verbose_name='Комментарий')
    category = TreeForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return f'{self.category} : {self.name}'

    class MPTTMeta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'