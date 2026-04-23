from django.shortcuts import render

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