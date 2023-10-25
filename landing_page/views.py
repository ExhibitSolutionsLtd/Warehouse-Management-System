from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProductCreationForm
from .models import Product

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
        products = Product.objects.all()
    context = {
        "product_form": product_form,
        "products": products
    }

    return render(request, 'landing_page/products.html', context)