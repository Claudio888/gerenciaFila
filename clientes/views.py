from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Concat
from django.db.models import Value



# Create your views here.

@login_required
def person_list(request):

    busca = request.GET.get('pesquisa', None)

    if busca:
        query = Person.objects.all()
        query_fullname = Person.objects.annotate(fullname=Concat('first_name', Value(' '), 'last_name'))
        persons = query_fullname.filter(fullname__icontains=busca)
    else:
        persons = Person.objects.all()

    return render(request, "person.html", {'persons':persons})

@login_required
def person_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form':form})

@login_required
def person_update(request,id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(request, 'person_form.html', {'form': form})

@login_required
def person_delete(request,id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance = person)

    if request.method == 'POST':
        person.delete()
        return redirect('person_list')

    return render(request,'person_delete_confirm.html', {'person': person})
