from django.shortcuts import render
from .models import Product, Category
from django.shortcuts import render, redirect
from django.db.models import Avg
from .models import Product, Category, CartItem, Subscriber, Rating

def home(request):
    context = {
        "title": "Головна",
        "pages": ["page1", "page2"]
    }
    return render(request, "main/home.html", context)


def page1(request):
    return render(request, "main/page.html", {"title": "Сторінка 1"})


def page2(request):
    return render(request, "main/page.html", {"title": "Сторінка 2"})

def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    context = {
        "products": products,
        "categories": categories,
    }

    return render(request, "main/home.html", context)
def category_page(request, category_id):
    categories = Category.objects.all()
    products = Product.objects.filter(category_id=category_id)

    context = {
        "products": products,
        "categories": categories,
    }

    return render(request, "main/home.html", context)

def product_page(request, product_id):
    product = Product.objects.get(id=product_id)
    categories = Category.objects.all()

    return render(request, "main/product.html", {
        "product": product,
        "categories": categories
    })

def category_page(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    categories = Category.objects.all()

    return render(request, "main/category.html", {
        "products": products,
        "categories": categories
    })

def product_page(request, product_id):
    product = Product.objects.get(id=product_id)
    categories = Category.objects.all()
    average_rating = product.ratings.aggregate(Avg('score'))['score__avg']

    if request.method == "POST":
        if "rating" in request.POST:
            Rating.objects.create(
                product=product,
                score=request.POST.get("rating")
            )
            return redirect('product', product_id=product.id)

        if "add_to_cart" in request.POST:
            CartItem.objects.create(product=product, quantity=1)
            return redirect('cart')

    return render(request, "main/product.html", {
        "product": product,
        "categories": categories,
        "average_rating": average_rating
    })


def cart_page(request):
    cart_items = CartItem.objects.all()
    return render(request, "main/cart.html", {"cart_items": cart_items})


def subscribe(request):
    if request.method == "POST":
        email = request.POST.get("email")
        Subscriber.objects.get_or_create(email=email)
    return redirect('home')
