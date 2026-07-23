from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    UpdateView,
    CreateView,
    View, DeleteView, )
from catalog.forms import ProductForm, CategoryForm, ProductModeratorForm
from catalog.models import Product, Category
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class PublishProductView(LoginRequiredMixin, View):
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)

        if not request.user.has_perm('product.can_unpublish_product'):
            return HttpResponseForbidden("У вас нет прав для снятия продукта с публикации.")

        product.is_publish = False
        product.save()

        return redirect('catalog:product_list')


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")
    # permission_required = 'catalog.add_product'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")
    # permission_required = 'catalog.edit_product'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm('can_unpublish_product') and user.has_perm('can_delete_product'):
            return ProductModeratorForm
        raise PermissionDenied


class CategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "catalog/category_form.html"
    success_url = reverse_lazy("catalog:home")
    permission_required = 'catalog.add_category'


class CategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "catalog/category_form.html"
    success_url = reverse_lazy("catalog:home")
    permission_required = 'catalog.edit_category'


class CategoryListView(ListView):
    model = Category


class ProductListView(ListView):
    model = Product


class ProductUnpublishListView(ListView):
    model = Product
    template_name = "catalog/unpublish_list.html"


class ProductDetailView(DetailView):
    model = Product


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(
            f"Спасибо {name}! Ваше сообщение получено. Благодарим за обратную связь."
        )
