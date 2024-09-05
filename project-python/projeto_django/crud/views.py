from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
def getperson(request):
    person = Person.objects.all().values()
    print(person)
    return render(request, 'templates/gridperson.html', {'person':person})

def addperson(request):
    if request.method == 'POST':
            person = Person()

            person.first_name = request.POST['first_name']
            person.last_name = request.POST['last_name']

            person.save()
            
            return redirect('/crud/getperson')


@csrf_exempt
def deleteperson(request, person_id):
    if request.method == "POST":
        person = get_object_or_404(Person, id=person_id)
        person.delete()
        return redirect('/crud/getperson')
    
@csrf_exempt
def editPerson(request):
    if request.method =='POST':
        try:
            persons = Person.objects.filter(pk=request.POST['id'])
            person = persons.first()
            person.first_name = request.POST['first_name']
            person.last_name = request.POST['last_name']
            person.save()
            return redirect('/crud/getperson')
        except:
            if person.exists():
                return HttpResponse("Error on save.", status=404)
            else:
                return HttpResponse("Person does not exist.", status=404)
           
def getEmpresa(request):
    empresa = Empresa.objects.all().values()
    print(empresa)
    return render(request, 'templates/folhinha/empresaCad.html', {'empresa':empresa})

def addEmpresa(request):
    if request.method == 'POST':
            empresa = Empresa()

            empresa.nome = request.POST['nome']
            empresa.email = request.POST['email']
            empresa.endereco = request.POST['endereco']
            empresa.telefone = request.POST['telefone']
            empresa.cnpj = request.POST['cnpj']

            empresa.save()
            
            return redirect('/crud/getEmpresa')


@csrf_exempt
def deleteempresa(request, empresa_id):
    if request.method == "POST":
        empresa = get_object_or_404(Empresa, id=empresa_id)
        empresa.delete()
        return redirect('/crud/getEmpresa')
    
@csrf_exempt
def editEmpresa(request):
    if request.method =='POST':
        try:
            empresas = Empresa.objects.filter(pk=request.POST['id'])
            empresa = empresas.first()
            empresa.nome = request.POST['nome']
            empresa.email = request.POST['email']
            empresa.endereco = request.POST['endereco']
            empresa.telefone = request.POST['telefone']
            empresa.cnpj = request.POST['cnpj']

            empresa.save()
            return redirect('/crud/getEmpresa')
        except:
            if empresa.exists():
                return HttpResponse("Error on save.", status=404)
            else:
                return HttpResponse("Person does not exist.", status=404)
           











def getCargo(request):
    cargo = Cargo.objects.all().values()
    print(cargo)
    return render(request, 'templates/folhinha/cargoCad.html', {'cargo':cargo})