from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'home/index.html')


def generic(request):
    return render(request, 'home/generic.html')


def elements(request):
    return render(request, 'home/elements.html')