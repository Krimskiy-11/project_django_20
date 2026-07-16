from django.db import models


class Blog(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="Заголовок", help_text="Введите название статьи"
    )
    text = models.TextField(
        verbose_name="Содержание",
        help_text="Раскройте суть статьи",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="images/",
        verbose_name="Фото",
        blank=True,
        null=True,
        help_text="Загрузите фото",
    )
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(
        default=True,
    )
    views = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "блог"
        verbose_name_plural = "блоги"
        ordering = ["title"]
