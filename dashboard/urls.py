from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard-index.html'),
    path('staff/', views.staff, name='dashboard-staff.html'),
    path('products/', views.products, name='dashboard-products.html'),
    path('orders/', views.orders, name='dashboard-orders.html')

]

