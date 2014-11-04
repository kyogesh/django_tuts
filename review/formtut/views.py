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
    initial_data = {'name':person.name, 'birth_place':person.birth_place, 'birth_date':person.birth_date}
    personform = PersonForm(initial=initial_data)
    return render(request, 'formtut/edit.html', {'person': person, 'personform':personform})

def save(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    personform = PersonForm(request.POST, instance=person)
    if personform.is_valid():
        print "Valid data"
        personform.save()
    else:
        print 'Invalid Data'
    
    return HttpResponseRedirect(reverse('forms:detail', args=(person.id,)))
