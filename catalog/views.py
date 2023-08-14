from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Product

main_title = 'Магазин продуктов'


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': main_title
    }


# def home(request):
#     context = {
#         'object_list': Product.objects.all(),
#         'title': main_title
#     }
#
#     return render(request, 'catalog/product_list.html', context)


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


class ProductDetailView(DetailView):
    model = Product
    extra_context = {
        'title': main_title
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.get(pk=self.kwargs.get('pk'))
        return context_data

# def products(request, pk):
#     context = {
#         'object_list': Product.objects.get(pk=pk),
#         'title': main_title
#     }
#     return render(request, 'catalog/product_detail.html', context)
