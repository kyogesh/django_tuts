from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import Poll, Choice

def index(request):
    polls = Poll.objects.all()
    return render(request,'index.html', {'polls':polls})

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'detail.html', {'poll': poll})

def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'results.html', {'poll': poll})

def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = poll.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {'poll':poll, 'err_msg':"You didn't selected any choice."})

    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('myapp:results', args=(poll.id,)))