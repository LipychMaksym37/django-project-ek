from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.category_page, name='category'),
]

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:product_id>/', views.product_page, name='product'),
    path('category/<int:category_id>/', views.category_page, name='category'),
]