from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

import catalog
from catalog.forms import ProductForm
from catalog.models import Product, Version

main_title = 'Магазин продуктов'


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': main_title
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # version_item = Version.objects.get(product_id=self.kwargs.get('pk'))
        version_list = Version.objects.all()

        context_data['version_list'] = version_list
        return context_data


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # version_item = Version.objects.get(product_id=self.kwargs.get('pk'))
        version_list = Version.objects.all()

        context_data['version_list'] = version_list
        return context_data

# def home(request):
#     context = {
#         'object_list': Product.objects.all(),
#         'title': main_title
#     }
#
#     return render(request, 'catalog/product_list.html', context)


class ProductDetailView(DetailView):
    model = Product
    extra_context = {
        'title': main_title
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.get(pk=self.kwargs.get('pk'))
        return context_data


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')


# def products(request, pk):
#     context = {
#         'object_list': Product.objects.get(pk=pk),
#         'title': main_title
#     }
#     return render(request, 'catalog/product_detail.html', context)

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
