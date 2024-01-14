from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Vehicules, Employe

class VehiculesListView(ListView):
    model = Vehicules
    template_name = 'vehicules_list.html' 
    context_object_name = 'vehicules_list'

class VehiculesDetailView(DetailView):
    model = Vehicules
    template_name = 'vehicules_detail.html' 
    context_object_name = 'vehicules'

class VehiculesCreateView(CreateView):
    model = Vehicules
    template_name = 'vehicules_form.html' 
    fields = ['Plaque', 'Marque', 'Place', 'Etat']

class VehiculesUpdateView(UpdateView):
    model = Vehicules
    template_name = 'vehicules_form.html' 
    fields = ['Plaque', 'Marque', 'Place', 'Etat']

class VehiculesDeleteView(DeleteView):
    model = Vehicules
    template_name = 'vehicules_confirm_delete.html' 
    success_url = '/vehicules/'

class EmployeListView(ListView):
    model = Employe
    template_name = 'employe_list.html' 
    context_object_name = 'employe_list'

class EmployeDetailView(DetailView):
    model = Employe
    template_name = 'employe_detail.html' 
    context_object_name = 'employe'

class EmployeCreateView(CreateView):
    model = Employe
    template_name = 'employe_form.html' 
    fields = ['IdEmploye', 'Nom', 'Prenom', 'Nationalite', 'CarteIdentite', 'Phone', 'Etat']

class EmployeUpdateView(UpdateView):
    model = Employe
    template_name = 'employe_form.html' 
    fields = ['IdEmploye', 'Nom', 'Prenom', 'Nationalite', 'CarteIdentite', 'Phone', 'Etat']

class EmployeDeleteView(DeleteView):
    model = Employe
    template_name = 'employe_confirm_delete.html' 
    success_url = '/employe/'
