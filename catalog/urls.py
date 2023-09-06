from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import CatalogConfig
from catalog.views import contact, ProductDetailView, ProductListView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, VersionCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('products/create/', never_cache(ProductCreateView.as_view()), name='product_create'),
    path('products/<int:pk>/update/', never_cache(ProductUpdateView.as_view()), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('versions/<int:pk>/create/', never_cache(VersionCreateView.as_view()), name='version_create'),

    path('contacts/', contact, name='contacts'),
    path('products/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='products'),
]
