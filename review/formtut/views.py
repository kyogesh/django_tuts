from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Person
from .forms import PersonForm

def index(request):
    persons=Person.objects.all()
    return render(request, 'formtut/index.html', {'persons': persons})

def detail(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    return render(request, 'formtut/details.html', {'person':person})

def edit(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    personform = PersonForm(instance=person)
    return render(request, 'formtut/edit.html', {'person': person, 'personform':personform})

def save(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    personform = PersonForm(instance=person)
    pf=PersonForm(request.POST)
    if pf.is_valid():
        print "Valid data", pf
    else:
        print 'Invalid Data'
    pf.save()
    return HttpResponseRedirect(reverse('forms:detail', args=(person.id,)))
