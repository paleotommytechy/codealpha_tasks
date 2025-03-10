from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'shop'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('products/', views.product, name='product'),
    path('products/category/<slug:category_slug>/', views.product, name='category'),
    path('product/<int:product_id>/', views.product_detail, name = 'product_detail'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )