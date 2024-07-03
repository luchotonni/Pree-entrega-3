from django.db.models import Q
from .models import Cartera, Remera, Pulsera
from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import CarteraForm, RemeraForm, PulseraForm


def insertar_cartera(request):
    if request.method == 'POST':
        form = CarteraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('insertar_cartera')
    else:
        form = CarteraForm()
    return render(request, 'shop/insertar_cartera.html', {'form': form})


def insertar_remera(request):
    if request.method == 'POST':
        form = RemeraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('insertar_remera')
    else:
        form = RemeraForm()
    return render(request, 'shop/insertar_remera.html', {'form': form})


def insertar_pulsera(request):
    if request.method == 'POST':
        form = PulseraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('insertar_pulsera')
    else:
        form = PulseraForm()
    return render(request, 'shop/insertar_pulsera.html', {'form': form})


def buscar_cartera(request):
    query = request.GET.get('q')
    resultados = []
    if query:
        resultados = Cartera.objects.filter(
            Q(nombre__icontains=query) | Q(descripcion__icontains=query))
    return render(request, 'shop/buscar_cartera.html', {'resultados': resultados})


def buscar_remera(request):
    query = request.GET.get('q')
    resultados = []
    if query:
        resultados = Remera.objects.filter(
            Q(nombre__icontains=query) | Q(descripcion__icontains=query))
    return render(request, 'shop/buscar_remera.html', {'resultados': resultados})


def buscar_pulsera(request):
    query = request.GET.get('q')
    resultados = []
    if query:
        resultados = Pulsera.objects.filter(
            Q(nombre__icontains=query) | Q(descripcion__icontains=query))
    return render(request, 'shop/buscar_pulsera.html', {'resultados': resultados})


def inicio(request):
    return render(request, 'shop/inicio.html')
