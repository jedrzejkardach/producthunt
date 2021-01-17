from django.shortcuts import render


def signup(request):

    return render(request=request, template_name='accounts/signup.html')


def login(request):

    return render(request=request, template_name='accounts/login.html')


def logout(request):
    # TODO Need to route to homepage
    return render(request=request, template_name='accounts/signup.html')