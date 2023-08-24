from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contact, ProductDetailView, ProductListView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    path('contacts/', contact, name='contacts'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='products'),
]
