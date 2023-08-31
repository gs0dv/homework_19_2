from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

import catalog
from catalog.forms import ProductForm, VersionForm
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

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:home')

    def get_last_number_version(self, number_pk):
        try:
            version = Version.objects.filter(product_id=number_pk, is_current_version=True)
            return version[0].version_number
        except Exception:
            return 0

    def deactivate_versions(self, number_pk):
        try:
            versions = Version.objects.filter(product_id=number_pk).update(is_current_version=False)

        except Exception:
            return 0

    def get_initial(self, **kwargs):
        pk = self.kwargs.get('pk')
        number_version = self.get_last_number_version(pk) + 1
        self.deactivate_versions(pk)
        return {'product': pk,
                'version_number': number_version}

    def my_deactivate(self, **kwargs):
        print(kwargs.get('pk'))


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
