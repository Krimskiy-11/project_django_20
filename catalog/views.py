from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from catalog.models import Product, Category


def home(request):
    categories = Category.objects.all()
    context = {'category': categories}
    return render(request, 'home.html', context)


def products_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product_list.html', context)


def product_detail(request, prod_id):
    product = get_object_or_404(Product, pk=prod_id)
    context = {'product': product}
    return render(request, 'product_detail.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        return HttpResponse(f'Спасибо {name}! Ваше сообщение получено. Благодарим за обратную связь.')
    return render(request, 'contacts.html')
