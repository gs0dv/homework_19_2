from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blogs.models import Blog


class BlogAllListView(ListView):
    model = Blog
    extra_context = {
        'title': 'Список всех блогов'
    }


class BlogListView(ListView):
    model = Blog
    extra_context = {
        'title': 'Список опубликованных блогов'
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogCreateView(CreateView):
    model = Blog
    fields = ('header', 'body', 'preview_image', 'is_published',)
    success_url = reverse_lazy('blogs:list')
    extra_context = {
        'title': 'Создание блога'
    }

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.header)
            new_mat.save()

        return super().form_valid(form)


class BlogDetailView(DetailView):
    model = Blog
    extra_context = {
        'title': 'Просмотр блога'
    }

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('header', 'body', 'preview_image', 'is_published',)
    success_url = reverse_lazy('blogs:list')
    extra_context = {
        'title': 'Редактировать блог'
    }

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.header)
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blogs:view', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs:list')
    extra_context = {
        'title': 'Удаление блога'
    }
