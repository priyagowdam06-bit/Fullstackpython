from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm  
from django.contrib import messages

def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)  
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')  
            return redirect('book_list')  
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/login.html', {'form': form})  

def logout_view(request):
    logout(request)
    return redirect('login')