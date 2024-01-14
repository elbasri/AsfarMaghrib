from django.contrib import admin
from .models import Vehicules, Ligne, Employe, Ticket, Branche, Service, Vend, Conduit, Travaille
from django.shortcuts import redirect
from django.urls import path
from .models import Employe, AuditEmploye
from django.db import transaction
from django.utils import timezone

admin.site.register(Vehicules)
admin.site.register(Ligne)
admin.site.register(Employe)
admin.site.register(Ticket)
admin.site.register(Branche)
admin.site.register(Service)
admin.site.register(Vend)
admin.site.register(Conduit)
admin.site.register(Travaille)

admin.site.register(AuditEmploye)