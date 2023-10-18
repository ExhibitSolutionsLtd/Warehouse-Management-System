from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.

# def login(request):
#     return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created Successfully {username}!')
            return redirect('dashboard')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form':form})


def profile(request):
    return render(request, 'profile.html')