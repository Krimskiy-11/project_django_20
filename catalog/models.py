from django.db import models


class Category(models.Model):
    category_name = models.CharField(
        max_length=100, verbose_name="Название", help_text="Введите название категории"
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание категории",
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
        max_length=100, verbose_name="Название", help_text="Введите название продукта"
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание продукта",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="images/",
        verbose_name="Фото",
        blank=True,
        null=True,
        help_text="Загрузите фото продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        blank=True,
        null=True,
        help_text="Выберите категорию продукта",
    )
    price = models.IntegerField(help_text="Введите цену продукта", verbose_name="Цена")

    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(auto_now=True, verbose_name="Дата изменения")

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["product_name"]
