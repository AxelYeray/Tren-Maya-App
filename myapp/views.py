from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "home.html")


def tickets(request):
    return render(request, "tickets.html")


def navegacion_i(request):
    return render(request, "navegacion_i.html")


def guia_turistica(request):
    return render(request, "guia_turistica.html")
