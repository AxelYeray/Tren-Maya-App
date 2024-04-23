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


def imagenes_puntos(request):
    return render(request, "imagenes_puntos.html")


def puntos_geo(request):
    return render(request, "puntos_geo.html")


def galeria(request):
    return render(request, "galeria.html")
