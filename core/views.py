from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect
from core.form import *

#Postos
def index(request):
    return render(request, 'admin-dashboard.html')

def pos_index(request):
    posto = postos.objects.all()
    pacote = {"postoChave": posto}
    return render(request, "pos-index.html", pacote)

def pos_create(request):
    form = postosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("lista_postos")
    
    pacote = {"form_postos": form}
    return render(request, "pos-create.html", pacote)

def  pos_show(request, id_vacina):
    posto = postos.objects.get(pk = id_vacina)
    pacote = {"postoChave": posto}
    return render(request, "pos-show.html",pacote)

def pos_update(request, id_posto):
    posto = postos.objects.get(pk = id_posto)
    form = postosForm(request.POST or None, instance = posto)
    if form.is_valid():
        form.save()
        return redirect("lista_postos")
    
    pacote = {"form_postos": form , "postoChave": posto}
    return render(request, "pos-update.html", pacote)

def delete_postos(request, id_posto):
    posto = postos.objects.get(pk = id_posto)
    posto.delete()
    return redirect("lista_postos")

#Vacinas
def vac_index(request):
    vacina = vacinas.objects.all()
    pacote = {"vacinaChave": vacina}
    return render(request, "vac-index.html", pacote)

def vac_create(request):
    form = vacinasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("lista_vacinas")
    
    pacote = {"form_vacinas": form}
    return render(request, "vac-create.html", pacote)

def  vac_show(request, id_vacina):
    vacina = vacinas.objects.get(pk = id_vacina)
    pacote = {"vacinaChave": vacina}
    return render(request, "vac-show.html",pacote)

def vac_update(request, id_vacina):
    vacina = vacinas.objects.get(pk = id_vacina)
    form = vacinasForm(request.POST or None, instance = vacina)
    if form.is_valid():
        form.save()
        return redirect("lista_vacinas")
    
    pacote = {"form_vacinas": form , "vacinaChave": vacina}
    return render(request, "vac-update.html", pacote)

def delete_vacinas(request, id_vacina):
    vacina = vacinas.objects.get(pk = id_vacina)
    vacina.delete()
    return redirect("lista_vacinas")