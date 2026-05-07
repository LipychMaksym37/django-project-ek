from django.urls import path
from . import views
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

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:product_id>/', views.product_page, name='product'),
    path('category/<int:category_id>/', views.category_page, name='category'),
    path('cart/', views.cart_page, name='cart'),
    path('subscribe/', views.subscribe, name='subscribe'),
]
urlpatterns = [
    path('', views.home, name='home'),

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),

    path('password-reset/', views.password_reset_view, name='password_reset'),
    path('password-reset-done/', views.password_reset_done_view, name='password_reset_done'),
]