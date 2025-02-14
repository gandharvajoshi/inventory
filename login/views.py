from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages  # Optional: For displaying messages to the user
from django.urls import reverse

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Use .get() to avoid KeyError
        password = request.POST.get('password')  # Use .get() to avoid KeyError
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect(reverse('mainpage')) # Redirect to a home page or dashboard
        else:
            # Optional: Use Django's messaging framework to show an error
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login/login_page.html', {'error': 'Invalid credentials'})
    
    # If it's a GET request, just render the login page
    return render(request, 'login/login_page.html')