from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect
from core.form import *

# Create your views here.
def index(request):
    return render(request, 'inicio.html')

def read_postos(request):
    posto = postos.objects.all()
    pacote = {"postoChave": posto}
    return render(request, "teste.html", pacote)

def create_postos(request):
    form = postosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("lista_postos")
    
    pacote = {"form_postos": form}
    return render(request, "create.html", pacote)

def update_postos(request, id_posto):
    posto = postos.objects.get(pk = id_posto)
    form = postosForm(request.POST or None, instance = posto)
    if form.is_valid():
        form.save()
        return redirect("lista_postos")
    
    pacote = {"form_postos": form}
    return render(request, "create.html", pacote)

def delete_postos(request, id_posto):
    posto = postos.objects.get(pk = id_posto)
    posto.delete()
    return redirect("lista_postos")


def read_vacinas(request):
    vacina = vacinas.objects.all()
    pacote = {"vacinaChave": vacina}
    return render(request, "vacinas.html", pacote)

def create_vacinas(request):
    form = vacinasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("lista_vacinas")
    
    pacote = {"form_vacinas": form}
    return render(request, "create_vacinas.html", pacote)

def update_vacinas(request, id_vacina):
    vacina = vacinas.objects.get(pk = id_vacina)
    form = vacinasForm(request.POST or None, instance = vacina)
    if form.is_valid():
        form.save()
        return redirect("lista_vacinas")
    
    pacote = {"form_vacinas": form}
    return render(request, "create_vacinas.html", pacote)

def delete_vacinas(request, id_vacina):
    vacina = vacinas.objects.get(pk = id_vacina)
    vacina.delete()
    return redirect("lista_vacinas")