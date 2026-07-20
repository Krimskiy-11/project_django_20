from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    UpdateView,
    CreateView,)
from catalog.forms import ProductForm, CategoryForm
from catalog.models import Product, Category
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "catalog/category_form.html"
    success_url = reverse_lazy("catalog:home")


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "catalog/category_form.html"
    success_url = reverse_lazy("catalog:home")


class CategoryListView(ListView):
    model = Category


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(
            f"Спасибо {name}! Ваше сообщение получено. Благодарим за обратную связь."
        )
