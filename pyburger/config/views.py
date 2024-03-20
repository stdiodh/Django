from django.http import HttpResponse
from burgers.models import Burger
from django.shortcuts import render

def main(request):
    return render(request, "main.html")

def burger_list(request):
    return render(request, "burger_list.html")

def burger_search(request):
    keyword = request.GET.get("keyword")

    if keyword is not None:
        burgers = Burger.objects.filter(name__contains=keyword)
    else:
        burgers = Burger.objects.none()

    context = {
        "burgers": burgers,
    }

    return render(request, "burger_search.html", context)