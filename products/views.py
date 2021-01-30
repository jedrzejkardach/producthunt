from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone


def home(request):
    products = Product.objects
    user_id = request.user.id
    return render(request=request, template_name='products/home.html', context={"products": products, "user_id": user_id})


@login_required
def create(request):
    if request.method == "POST":
        if request.POST["title"] and request.POST["body"] and request.POST["url"] and request.FILES["icon"] and request.FILES["image"]:
            product = Product()
            product.title = request.POST["title"]
            product.body = request.POST["body"]
            if request.POST["url"].startswith("http://") or request.POST["url"].startswith("https://"):
                product.url = request.POST["url"]
            else:
                product.url = "http://" + request.POST["url"]
            product.icon = request.FILES["icon"]
            product.image = request.FILES["image"]
            product.pub_date = timezone.datetime.now()
            product.hunter = request.user
            product.save()
            return redirect('/products/' + str(product.id))

        else:
            return render(request=request, template_name='products/create.html', context={"error": "all values are required"})
    else:
        return render(request=request, template_name='products/create.html')


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    user_id = request.user.id
    return render(request=request, template_name='products/detail.html', context={"product": product, "user_id": user_id})


@login_required(login_url="/accounts/login")
def upvote(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=product_id)
        current_user_id = request.user.id
        if current_user_id in product.upvoted_by:
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        else:
            product.votes_total += 1
            product.upvoted_by = product.upvoted_by + [current_user_id]
            product.save()
            return redirect('/products/' + str(product.id))

