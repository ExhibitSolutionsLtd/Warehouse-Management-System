from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProductCreationForm, OrderCreationForm, CustomerCreationForm, SupplierCreationForm
from .models import Product, Order, Customer, Supplier
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.utils import timezone

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
    pending = Order.objects.filter(status = 'Pending')
    transit = Order.objects.filter(status = 'GIT')
    context = {
        "inventory":inventory,
        "pending":pending,
        "transit":transit,
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

        paginator_prods = Paginator(products, 8)
        page_number = request.GET.get('page')
        products_page = paginator_prods.get_page(page_number)
    context = {
        "product_form": product_form,
        "products": products,
        "products_page":products_page
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
        paginator_inbound = Paginator(inbound_orders, 8)
        page_number_in = request.GET.get('page')
        customers_page_in = paginator_inbound.get_page(page_number_in)

        paginator_outbound = Paginator(outbound_orders, 8)
        page_number_out = request.GET.get('page')
        customers_page_out = paginator_outbound.get_page(page_number_out)
    context = {
        "order_form": order_form,
        "inbound_orders": inbound_orders,
        "outbound_orders":outbound_orders,
        "customers_page_in":customers_page_in,
        "customers_page_out":customers_page_out
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

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'landing_page/product_update.html'
    fields = [ "sku", "item_name", "quantity", "category", "location", "description", "product_image",]
    success_url = reverse_lazy('products')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, f'Item edited successfully!')
        return super().form_valid(form)
    
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'landing_page/product_delete.html'
    success_url = reverse_lazy('products')

    def form_valid(self, form):
        messages.success(self.request, f'Item deleted successfully!')
        return super().form_valid(form)

class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'landing_page/order_update.html'
    fields = [ "order_id", "item", "order_type", "total_items", "status", "notes"]
    success_url = reverse_lazy('orders')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, f'Order edited successfully!')
        return super().form_valid(form)
    
class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'landing_page/order_delete.html'
    success_url = reverse_lazy('orders')

    def form_valid(self, form):
        messages.success(self.request, f'Order deleted successfully!')
        return super().form_valid(form)
    

class SupplierUpdateView(UpdateView):
    model = Supplier
    template_name = 'landing_page/supplier_update.html'
    fields = ['sup_f_name', 'sup_l_name', 'email', 'mobile_no', 'address', 'notes']
    success_url = reverse_lazy('suppliers')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, f'Supplier details edited successfully!')
        return super().form_valid(form)
    
class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = 'landing_page/supplier_delete.html'
    success_url = reverse_lazy('suppliers')

    def form_valid(self, form):
        messages.success(self.request, f'Suppliers details deleted successfully!')
        return super().form_valid(form)
    
class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'landing_page/customer_update.html'
    fields = ['cust_f_name', 'cust_l_name', 'email', 'mobile_no', 'address', 'notes']
    success_url = reverse_lazy('customers')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, f'Customer details edited successfully!')
        return super().form_valid(form)
    
class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'landing_page/customer_delete.html'
    success_url = reverse_lazy('customers')

    def form_valid(self, form):
        messages.success(self.request, f'Customers details deleted successfully!')
        return super().form_valid(form)
    
class OrderDetailView(DetailView):
    model = Order
    template_name = 'landing_page/order_detail.html'
    context_object_name = 'order_detail'


def reports(request):
    today = timezone.localdate()
    todays_inventory = Product.objects.filter(item_created_at__date=today)
    pending = Order.objects.filter(status = 'Pending')

    context = {
        'today':today,
        'todays_inventory':todays_inventory,
        'pending':pending
    }
    return render(request, 'landing_page/reports.html', context)