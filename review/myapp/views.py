from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.utils import timezone

from ipdb import set_trace

from .forms import PollForm, PollUserForm
from .models import Poll, Choice, PollUser


def index(request):
    polls = Poll.objects.all()
    return render(request, 'myapp/index.html', {'polls': polls})


def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'myapp/detail.html', {'poll': poll})


def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'myapp/results.html', {'poll': poll})


def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = poll.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'myapp/detail.html',
                      {'poll': poll,
                       'err_msg': "You didn't selected any choice."})

    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('myapp:results',
                                            args=(poll.id, )))


def register(request):
    registered = False
    password_matched = None
    if request.method == 'POST':
        user_form = PollUserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save(commit=False)
            print request.POST['confirm_password'] == user.password
            if user.password == request.POST['confirm_password']:
                password_matched = True
                print "Password matches"
                user.set_password(user.password)
                user.save()
                registered = True
            else:
                password_matched = False                
                registered=False

    else:
        user_form = PollUserForm()

    return render(request,
                  'myapp/register.html',
                  {'user_form': user_form,
                   'registered': registered,
                   'password_matched':password_matched})


def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('myapp:index'))
            else:
                return HttpResponse("Your Poll account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render_to_response('myapp/login.html',
                                  {}, RequestContext(request))


@login_required
def signoff(request):

    logout(request)

    return HttpResponseRedirect(reverse('myapp:index'))


@login_required
def addpoll(request):
    if request.method == 'POST':
        poll_form = PollForm(data=request.POST)
        print request.POST
        choices=[e for e in request.POST.keys() if e.startswith('choice')]
        choices.sort()
        if poll_form.is_valid and choices:
            new_poll = poll_form.save(commit=False)
            new_poll.pub_date = timezone.now()
            new_poll.created_by = PollUser.objects.get(username=request.user)
            new_poll.save()
            for each in choices:
                choice = Choice(poll_id=new_poll.id,
                                choice=request.POST[each])
                choice.save()
            return HttpResponseRedirect(reverse('myapp:detail',
                                                args=(new_poll.id, )))
        else:
            poll_form.errors
    elif request.method=='GET' and not request.user:
        return HttpResponseRedirect(reverse('myapp:signin'))
    else:
        poll_form = PollForm()

    return render(request,
                  'myapp/add_poll.html',
                  {'poll_form': poll_form, })
