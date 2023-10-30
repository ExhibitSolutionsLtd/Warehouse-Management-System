from django.urls import path
from . import views
from .views import ProductUpdateView

urlpatterns = [
    path('', views.landing_page, name="landing-page"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('products/', views.products, name="products"),
    path('orders/', views.orders, name="orders"),
    path('customers/', views.customers, name="customers"),
    path('suppliers/', views.suppliers, name="suppliers"),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name="products-update"),

]