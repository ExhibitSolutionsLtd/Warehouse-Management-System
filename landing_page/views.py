from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProductCreationForm, OrderCreationForm, CustomerCreationForm, SupplierCreationForm
from .models import Product, Order, Customer, Supplier
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.

posts = [
    {'author':'Ngugi wa Thiong\'o', 'content': 'This is section one', 'date_posted': 'August 20,2023'},
    {'author':'Ken Walibora', 'content': 'Kifo Kisimani', 'date_posted': 'July 20,2023'},
]
def landing_page(request):
    context = {
        'posts':posts
    }
    return render(request, "landing_page/index.html", context)

@login_required
def dashboard(request):
    inventory = Product.objects.all()
    context = {
        "inventory":inventory
    }
    return render(request, 'landing_page/dashboard.html', context)


def products(request):
    if request.method == "POST":
        product_form = ProductCreationForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.instance.user = request.user
            product_form.save()
            messages.success(request, f'Product Added Successfully!')
            return redirect('products')
    else:
        product_form = ProductCreationForm()
        products = Product.objects.all().order_by('-pk')
    context = {
        "product_form": product_form,
        "products": products
    }

    return render(request, 'landing_page/products.html', context)


def orders(request):
    if request.method == "POST":
        order_form = OrderCreationForm(request.POST)
        if order_form.is_valid():
            order_form.save()
            messages.success(request, f'Order Added Successfully!')
            return redirect('orders')
    else:
        order_form = OrderCreationForm()
        inbound_orders = Order.objects.filter(order_type = 'Inbound')
        outbound_orders = Order.objects.filter(order_type = 'Outbound')
    context = {
        "order_form": order_form,
        "inbound_orders": inbound_orders,
        "outbound_orders":outbound_orders
    }

    return render(request, 'landing_page/orders.html', context)

def customers(request):
    if request.method == "POST":
        customer_form = CustomerCreationForm(request.POST)
        if customer_form.is_valid():
            customer_form.save()
            messages.success(request, f'Customer Added Successfully!')
            return redirect('customers')
    else:
        customer_form = CustomerCreationForm()
        customers = Customer.objects.all()

        paginator = Paginator(customers, 8)
        page_number = request.GET.get('page')
        customers_page = paginator.get_page(page_number)
    context = {
        "customer_form": customer_form,
        "customers":customers,
        "customers_page": customers_page
    }

    return render(request, 'landing_page/customers.html', context)

def suppliers(request):
    if request.method == "POST":
        suppliers_form = SupplierCreationForm(request.POST)
        if suppliers_form.is_valid():
            suppliers_form.save()
            messages.success(request, f'Supplier Added Successfully!')
            return redirect('suppliers')
    else:
        suppliers_form = SupplierCreationForm()
        suppliers = Supplier.objects.all()

        paginator = Paginator(suppliers, 8)
        page_number = request.GET.get('page')
        suppliers_page = paginator.get_page(page_number)
    context = {
        "supplier_form": suppliers_form,
        "suppliers":suppliers,
        "suppliers_page": suppliers_page
    }

    return render(request, 'landing_page/suppliers.html', context)

