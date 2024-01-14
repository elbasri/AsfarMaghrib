from django.urls import path
from . import views

urlpatterns = [
    path('vehicules/', views.VehiculesListView.as_view(), name='vehicules-list'),
    path('vehicules/<int:pk>/', views.VehiculesDetailView.as_view(), name='vehicules-detail'),
    path('vehicules/create/', views.VehiculesCreateView.as_view(), name='vehicules-create'),
    path('vehicules/<int:pk>/update/', views.VehiculesUpdateView.as_view(), name='vehicules-update'),
    
    path('employe/', views.EmployeListView.as_view(), name='employe-list'),
    path('employe/<int:pk>/', views.EmployeDetailView.as_view(), name='employe-detail'),
    path('employe/create/', views.EmployeCreateView.as_view(), name='employe-create'),
    path('employe/<int:pk>/update/', views.EmployeUpdateView.as_view(), name='employe-update'),
]
