from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm  # or your custom LoginForm
from django.contrib import messages

def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)  # FIX 1: comma not dot
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')  # FIX 2: f-string
            return redirect('book_list')  # FIX 3: quotes around url name
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/login.html', {'form': form})  # FIX 4: space after comma

def logout_view(request):
    logout(request)
    return redirect('login')  # FIX 5: quotes around url name