from django.urls import path

from blogs.apps import BlogsConfig
from blogs.views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView, BlogAllListView

app_name = BlogsConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('list/', BlogAllListView.as_view(), name='list_all'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete')
]
