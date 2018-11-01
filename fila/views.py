from django.shortcuts import render, redirect, get_object_or_404
from .forms import FilaForm
from django.http import HttpResponse
from clientes.models import Person
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout



# Create your views here.

class Fila():
    #def __init__(self):
    #    self.fila =[]

    def crialista(self):
        self.fila = []

    def inserir(self, elemento):
        self.fila.append(elemento)

    def retirar(self):
        if not self.vazia():
            return self.fila.pop(0)
        else:
            return 0

    def tamanho(self):
        return len(self.fila)

    def vazia(self):
        return self.tamanho() == 0

fila = Fila()
fila.crialista()

@login_required
def AddFila(request):
    form = FilaForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            valor=form.cleaned_data['nrfid']
            fila.inserir(valor)
            #print(fila.tamanho())
            form = FilaForm()
        return render(request, 'add.html',{'form': form})
    else:
        return render(request, 'add.html', {'form': form})

@login_required
def ChamarFila(request):
    if request.method == "POST":
            removido = fila.retirar()
            persons = Person.objects.filter(rfid=removido)
            tamanhofila = fila.tamanho()
            print(tamanhofila)
            return render(request, "chamar.html", {'persons': persons,'tamanhofila':tamanhofila})
    else:
        tamanhofila = fila.tamanho()
        return render(request, "chamar.html",{'tamanhofila':tamanhofila})


def Home(request):
    return render(request,'home.html')

def mylogout(request):
    logout(request)
    return redirect('home')