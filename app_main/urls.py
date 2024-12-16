from django.urls import path

from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('detail/<int:product_id>/', views.product_detail, name='detail'),
    path('add-to-cart/<int:product_id/', views.add_to_cart, name='add_to_cart'),
]
