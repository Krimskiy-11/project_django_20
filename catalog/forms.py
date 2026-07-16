from django import forms
from django.core.exceptions import ValidationError

from .models import Product, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["product_name", "description", "category", "price"]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["product_name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите название продукта"}
        )

        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание продукта"}
        )

        self.fields["category"].widget.attrs.update(
            {
                "class": "form-select",
                # 'class': "form-select",
                "placeholder": "Выберите категорию",
            }
        )

        self.fields["price"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите цену продукта"}
        )

    def clean_product_name(self):
        name = self.cleaned_data.get("product_name")
        error_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]

        if name in error_words:
            raise ValidationError("Запрещенное наименование в названии")
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        description_list = description.split()
        error_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]

        for object_description in description_list:
            if object_description in error_words:
                raise ValidationError("Запрещенное наименование в описании")
        return description

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError("Цена не может быть меньше нуля")
        return price


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)

        self.fields["category_name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите название категории"}
        )

        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание категории"}
        )
