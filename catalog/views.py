from django.shortcuts import render

from catalog.models import Product

main_title = 'Магазин продуктов'


def home(request):
    context = {
        'object_list': Product.objects.all(),
        'title': main_title
    }

    return render(request, 'catalog/home.html', context)


def contact(request):
    content = {
        'title': main_title
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"{name} ({phone}): {message}")
    return render(request, 'catalog/contacts.html', content)


def products(request, pk):
    context = {
        'object_list': Product.objects.get(pk=pk),
        'title': main_title
    }
    return render(request, 'catalog/products.html', context)
