from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProductCreationForm

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
        product_form = ProductCreationForm()
        if product_form.is_valid():
            product_form.save()
            messages.success(request, f'Product Added Successfully!')
            return redirect('products')
    else:
        product_form = ProductCreationForm()

    context = {
        "product_form": product_form
    }

    return render(request, 'landing_page/products.html', context)