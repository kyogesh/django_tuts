from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from .models import Poll

def index(request):
    polls = Poll.objects.all()
    return render(request,'index.html', {'polls':polls})

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'detail.html', {'poll': poll})

def results(request, poll_id):
    return render(request, 'results.html')

def vote(request, poll_id):
    return render(request, 'vote.html')