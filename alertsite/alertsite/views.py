from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserChangeForm
from alert.models import Event
from comment.models import Comment
# Create your views here.


def block_to_auth(request, page, context):
    if request.user.is_authenticated():
        return redirect('/')
    else:
        return render(request, page, context)


def check_auth(request, page, context):
    if request.user.is_authenticated():
        return render(request, page, context)
    else:
        return redirect('/reg_auth')


def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request, password=0):
    if request.method != 'POST':
        return redirect('/')
    username = request.POST['username']
    if password == 0:
        password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
    return authentification(request, er=1)


def update_user(request):
    if request.method != 'POST':
        return redirect('/')
    user = request.user
    form = UserChangeForm(request.POST)
    if form.is_valid():
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        return redirect('/')
    return user(request, er=1)


def registration(request, er=0):
    if request.user.is_authenticated():
        return redirect('/')
    form = UserCreationForm
    er = int(er)
    context = {'form': form, 'er': er}
    return render(request, 'reg.html', context)


def create_user(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return login(request, password=request.POST['password1'])
    return registration(request, er=1)


def authentification(request, er=0):
    if request.user.is_authenticated():
        return redirect('/')
    form = AuthenticationForm
    er = int(er)
    context = {'form': form, 'er': er}
    return render(request, 'auth.html', context)


def reg_auth(request):
    if request.user.is_authenticated():
        return redirect('/')
    return render(request, 'reg_auth.html')


def user(request, er=0):
    if request.user.is_authenticated() is False:
        return render(request, 'reg_auth.html')
    er = int(er)
    form = UserChangeForm
    context = {'form': form, 'er': er}
    return render(request, 'user.html', context)


def index(request):
    if request.user.is_authenticated() is False:
        return render(request, 'reg_auth.html')
    invites = Event.objects.filter(invite_list=request.user).count()
    event_list = Event.objects.filter(
        participants=request.user
    ).order_by('event_time')
    events = list()
    not_active = list()
    for i in event_list:
        if i.is_active():
            events.append(i)
        else:
            not_active.append(i)
    not_active = len(not_active)
    for event in events:
        event.count_comments = Comment.objects.filter(
            event=event.id,
            enable=True
        ).count()
        event.participant_list = event.participants.all()
    context = {'events': events, 'invites': invites, 'not_active': not_active}
    return render(request, 'loyout.html', context)


def not_active(request):
    if request.user.is_authenticated() is False:
        return render(request, 'reg_auth.html')
    invites = Event.objects.filter(invite_list=request.user).count()
    event_list = Event.objects.filter(
        participants=request.user
    ).order_by('event_time')
    events = list()
    for i in event_list:
        if not i.is_active():
            events.append(i)
    not_active = len(events)
    for event in events:
        event.count_comments = Comment.objects.filter(
            event=event.id,
            enable=True
        ).count()
        event.participant_list = event.participants.all()
    context = {'events': events, 'invites': invites, 'not_active': not_active}
    return render(request, 'loyout.html', context)


def invites(request):
    if request.user.is_authenticated() is False:
        return render(request, 'reg_auth.html')
    invites = Event.objects.filter(invite_list=request.user).count()
    event_list = Event.objects.filter(
        invite_list=request.user
    ).order_by('event_time')
    event_list_2 = Event.objects.filter(participants=request.user)
    events = list()
    for i in event_list:
        events.append(i)
    not_active = list()
    for i in event_list_2:
        if not i.is_active():
            not_active.append(i)
    not_active = len(not_active)
    invite = True
    for event in events:
        event.count_comments = Comment.objects.filter(
            event=event.id,
            enable=True
        ).count()
    context = {
        'events': events,
        'invites': invites,
        'invite': invite,
        'not_active': not_active
    }
    return render(request, 'loyout.html', context)
