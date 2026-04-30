from django.shortcuts import render
from .models import Product, Category

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