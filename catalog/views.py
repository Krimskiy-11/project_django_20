from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from catalog.models import Product, Category


class CategoryListView(ListView):
    model = Category

class ProductListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product

class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        message = request.POST.get('message')
        return HttpResponse(f'Спасибо {name}! Ваше сообщение получено. Благодарим за обратную связь.')