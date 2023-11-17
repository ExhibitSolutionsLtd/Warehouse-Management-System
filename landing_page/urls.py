from django.urls import path
from . import views
from .views import ProductUpdateView, ProductDeleteView, OrderUpdateView,OrderDeleteView, SupplierUpdateView, SupplierDeleteView, CustomerUpdateView, CustomerDeleteView, OrderDetailView, ProductDetailsView, TransferCreateView, TransfersListsView

urlpatterns = [
    path('', views.landing_page, name="landing-page"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('products/', views.products, name="products"),
    path('orders/', views.orders, name="orders"),
    path('customers/', views.customers, name="customers"),
    path('suppliers/', views.suppliers, name="suppliers"),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name="products-update"),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name="product-delete"),
    path('order/<int:pk>/edit/', OrderUpdateView.as_view(), name="orders-update"),
    path('order/<int:pk>/delete/', OrderDeleteView.as_view(), name="order-delete"),
    path('supplier/<int:pk>/edit/', SupplierUpdateView.as_view(), name="suppliers-update"),
    path('supplier/<int:pk>/delete/', SupplierDeleteView.as_view(), name="supplier-delete"),
    path('customer/<int:pk>/edit/', CustomerUpdateView.as_view(), name="customers-update"),
    path('customer/<int:pk>/delete/', CustomerDeleteView.as_view(), name="customer-delete"),
    path('order/<int:pk>/detail/', OrderDetailView.as_view(), name="order-detail"),
    path('product/<int:pk>/detail/', ProductDetailsView.as_view(), name="product-detail"),
    path('reports', views.reports, name="reports"),
    path('transfers/create', TransferCreateView.as_view(), name="transfers"),
    path('transfers/', TransfersListsView.as_view(), name="transfers-list"),
    path('scan/', views.scanner, name="scanner"),

]