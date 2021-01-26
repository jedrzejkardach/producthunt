from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
    if request.method == 'POST':
        # user has info and wants to send it
        if request.POST['password1'] == request.POST['password2']:
            try:
                _ = User.objects.get(username=request.POST['username'])
                return render(request=request, template_name='accounts/signup.html', context={'error': 'Username is already taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request=request, template_name='accounts/signup.html',
                          context={'error': 'Passwords must match'})
    else:
        # user wants to enter info
        return render(request=request, template_name='accounts/signup.html')


def login(request):
    # check if method post, if yes then we will start log in procedure
    # else it is simple get and we just return the website
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            try:
                _ = User.objects.get(username=request.POST['username'])
                return render(request=request, template_name='accounts/login.html',
                              context={'error': 'Password is incorrect'})
            except User.DoesNotExist:
                return render(request=request, template_name='accounts/login.html',
                              context={'error': 'User does not exist'})
    else:
        return render(request=request, template_name='accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
