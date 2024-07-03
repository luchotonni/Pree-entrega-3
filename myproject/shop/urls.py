from django.urls import path
from . import views

urlpatterns = [
    path('insertar_cartera/', views.insertar_cartera, name='insertar_cartera'),
    path('insertar_remera/', views.insertar_remera, name='insertar_remera'),
    path('insertar_pulsera/', views.insertar_pulsera, name='insertar_pulsera'),
    path('buscar_cartera/', views.buscar_cartera, name='buscar_cartera'),
    path('buscar_remera/', views.buscar_remera, name='buscar_remera'),
    path('buscar_pulsera/', views.buscar_pulsera, name='buscar_pulsera'),
    path('', views.inicio, name='inicio'),
]
