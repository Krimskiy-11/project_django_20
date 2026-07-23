from django.db import models

from users.models import CustomUser


class Category(models.Model):
    category_name = models.CharField(
        max_length=100, verbose_name="Название",
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["category_name"]


class Product(models.Model):
    product_name = models.CharField(
        max_length=100, verbose_name="Название",
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="images/",
        verbose_name="Фото",
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        blank=True,
        null=True,
    )
    price = models.IntegerField(verbose_name="Цена")
    is_publish = models.BooleanField(default=False, verbose_name="Статус публикации",)
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name="Владелец",
        blank=True,
        null=True,
    )

    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(auto_now=True, verbose_name="Дата изменения")

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["product_name"]
        permissions = [
            ('can_unpublish_product', 'Can unpublish product'),
            ('can_delete_product', 'Can delete product'),
        ]
