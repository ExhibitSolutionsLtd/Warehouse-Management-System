from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProductCreationForm, OrderCreationForm
from .models import Product, Order, Customer, Supplier

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

def dashboard(request):
    return render(request, 'landing_page/dashboard.html')


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
            order_form.instance.user = request.user
            order_form.save()
            messages.success(request, f'Order Added Successfully!')
            return redirect('orders')
    else:
        order_form = OrderCreationForm()
        orders = Order.objects.all().order_by('-pk')
    context = {
        "order_form": order_form,
        "orders": orders
    }

    return render(request, 'landing_page/orders.html', context)