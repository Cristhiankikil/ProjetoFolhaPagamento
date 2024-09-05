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

def getCargo(request):
    cargo = Cargo.objects.all().values()
    print(cargo)
    return render(request, 'templates/folhinha/cargoCad.html', {'cargo':cargo})