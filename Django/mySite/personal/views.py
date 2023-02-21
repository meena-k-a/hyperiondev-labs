from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def about_me(request):
    return render(request, "about_me.html")

def shopping_site(request):
    return render(request, "shopping_site.html")
