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


def latest_polls():
    return Poll.objects.order_by('-pub_date')[:5]


def index(request):
    polls = Poll.objects.all()
    return render(request, 'myapp/index.html',
                  {'polls': polls,
                   'latest_polls': latest_polls()})


def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'myapp/detail.html',
                  {'poll': poll,
                   'latest_polls': latest_polls()})


def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'myapp/results.html',
                  {'poll': poll,
                   'latest_polls': latest_polls()})


@login_required
def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    try:
        user = PollUser.objects.get(username=request.user)
    except:
        user = None
    if poll.created_by != user:
        print "same User"
        try:
            selected_choice = poll.choice_set.get(pk=request.POST['choice'])
        except(KeyError, Choice.DoesNotExist):
            return render(request, 'myapp/detail.html',
                          {'poll': poll,
                           'err_msg': "You didn't selected any choice.",
                           'latest_polls': latest_polls(), })
        else:
            selected_choice.votes += 1
            selected_choice.save()
    else:
        return render(request, 'myapp/detail.html',
                      {'poll': poll,
                       'err_msg': "You can not vote on your own Poll.",
                       'latest_polls': latest_polls(), })
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
                user.set_password(user.password)
                user.save()
                registered = True
            else:
                password_matched = False
                registered = False

    else:
        user_form = PollUserForm()

    return render(request,
                  'myapp/register.html',
                  {'user_form': user_form,
                   'registered': registered,
                   'password_matched': password_matched,
                   'latest_polls': latest_polls(), })


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
            login_err = 'Invalid username or password.'
            return render_to_response('myapp/login.html',
                                      {'login_err': login_err},
                                      RequestContext(request))

    else:

        return render_to_response('myapp/login.html',
                                  {'latest_polls': latest_polls()},
                                  RequestContext(request))


@login_required
def signoff(request):

    logout(request)

    return HttpResponseRedirect(reverse('myapp:index'))


@login_required
def addpoll(request):
    choice_err = ''
    if request.method == 'POST':
        poll_form = PollForm(data=request.POST)
        choices = [e for e in request.POST.keys() if e.startswith('choice')]
        choices.sort()
        if poll_form.is_valid and len(choices) > 2:
            new_poll = poll_form.save(commit=False)
            new_poll.pub_date = timezone.now()
            new_poll.created_by = PollUser.objects.get(username=request.user)
            new_poll.save()
            for each in choices:
                if request.POST[each]:
                    choice = Choice(poll_id=new_poll.id,
                                    choice=request.POST[each])
                    choice.save()
            print new_poll
            if new_poll.choice_set:
                return HttpResponseRedirect(reverse('myapp:detail',
                                                    args=(new_poll.id, )))
            else:
                print 'no choice set'
                choice_err = "Please add at least three choices."
        else:
            poll_form.errors
            choice_err = "Please add at least three choices."

    elif request.method == 'GET' and not request.user:
        return HttpResponseRedirect(reverse('myapp: signin'))
    else:
        print "Error in Choices", choice_err
        poll_form = PollForm()

    return render(request,
                  'myapp/add_poll.html',
                  {'poll_form': poll_form,
                   'choice_err': choice_err,
                   'latest_polls': latest_polls(), })
