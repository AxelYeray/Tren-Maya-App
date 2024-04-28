from django.shortcuts import render
from .models import Project, Ticket, Galeria


# Create your views here.
def home(request):
    projects = Project.objects.all()

    return render(request, "home.html", {"projects": projects})


def tickets(request):
    imagenes = Ticket.objects.all()  # Cambiado de 'imagen' a 'imagenes'
    return render(
        request, "tickets.html", {"imagenes": imagenes}
    )  # Cambiado de 'imagen' a 'imagenes'


def galeria(request):
    imagenes = Galeria.objects.all()  # Cambiado de 'imagen' a 'imagenes'
    return render(
        request, "galeria.html", {"imagenes": imagenes}
    )  # Cambiado de 'imagen' a 'imagenes'
