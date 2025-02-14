from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
        else:
            user = User.objects.create_user(username=username, password=password1)
            user.save()
            messages.success(request, "Account created successfully.")
            return redirect('login_view')

    return render(request, 'signup/signup.html')

