from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect
from core.form import *
from django.utils import timezone
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

def  pos_show(request, id_posto):
    posto = postos.objects.get(pk = id_posto)
    pacote = {"postoChave": posto}
    return render(request, "pos-show.html",pacote)

def  pos_vac_index(request, id_posto):
    posto = postos.objects.get(pk = id_posto)
    vacina = vacinas.objects.filter(vac_posto = id_posto)
    pacote = {"postoChave": posto, "vacinasChave": vacina}
    return render(request, "pos-vac-index.html",pacote)

def pos_vac_create(request,id_posto):
    form = vacinasForm(request.POST or None)
    form.fields["vac_posto"].initial = id_posto
    if form.is_valid():
        form.save()       
        return redirect("lista_vacinas")
    pacote = {"form_vacinas": form}
    return render(request, "pos-vac-create.html", pacote)

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

def vac_day_index(request):
    hoje = timezone.now()
    data = hoje.isoweekday()
    vacina = vacinas.objects.filter(vac_disponibilidade = 1, vac_dias = data)
    pacote = {"vacinaChave": vacina}
    return render(request, "vac-day-index.html", pacote)

def vac_create(request):
    form = vacinasForm(request.POST or None)
    if form.is_valid():
        form.save()       
        return redirect("lista_vacinas")
    pacote = {"form_vacinas": form}
    return render(request, "vac-create.html", pacote)

def  vac_show(request, id_vacina):
    vacina = vacinas.objects.get(pk = id_vacina)
    dias = vacina.vac_dias.all()
    pacote = {"vacinaChave": vacina, "dias":dias}
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