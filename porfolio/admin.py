from django.contrib import admin
from .models import Project, Ticket, Galeria


# Register your models here.
admin.site.register(Project)
admin.site.register(Ticket)
admin.site.register(Galeria)