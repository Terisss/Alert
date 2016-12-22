from django.shortcuts import get_object_or_404, redirect
from alertsite.views import check_auth
from .models import Event
from comment.models import Comment
from comment.forms import CommentsForm
from alert.forms import CreateEventForm, ChangeEventForm
from datetime import datetime, timedelta
# Create your views here.


def event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    comments = Comment.objects.filter(
        event=event_id,
        enable=True
    ).order_by('-pub_date')
    count_comments = comments.count()
    form = CommentsForm()
    members = event.participants.all()
    invite_list = event.invite_list.all()
    permission = False
    for member in members:
        if member == request.user:
            permission = True
    for inviter in invite_list:
        if inviter == request.user:
            permission = True
    if permission:
        context = {
            'event': event,
            'members': members,
            'invite_list': invite_list,
            'comments': comments,
            'count_comments': count_comments,
            'form': form
        }
        page = 'event.html'
        return check_auth(request, page, context)
    else:
        return redirect('/')


def event_constructor(request, er=0):
    er = int(er)
    form = CreateEventForm()
    context = {'form': form, 'er': er}
    page = 'event_constructor.html'
    return check_auth(request, page, context)


def event_editor(request, event_id, er=0):
    er = int(er)
    event = get_object_or_404(Event, pk=event_id)
    if request.user != event.host:
        return redirect('/')
    form = ChangeEventForm()
    invite_list = event.invite_list.all()
    members = event.participants.all()
    context = {
        'form': form,
        'er': er,
        'event': event,
        'invite_list': invite_list,
        'members': members
    }
    page = 'event_editor.html'
    return check_auth(request, page, context)


def create_event(request):
    if request.method != 'POST':
        return redirect('/')
    form = CreateEventForm(request.POST)
    data = request.POST
    if form.is_valid():
        event_time = datetime(
            year=int(data['year']),
            month=int(data['month']),
            day=1,
            hour=int(data['hour']),
            minute=int(data['minute'])
        ) + timedelta(int(data['day']) - 1)
        if event_time < datetime.now():
            return event_constructor(request, er=1)
        obj = form.save(commit=False)
        obj.event_time = event_time
        obj.host = request.user
        obj.save()
        event = Event.objects.get(pk=obj.id)
        event.participants.add(request.user)
        invite = data.getlist('invite_list')
        for i in invite:
            if int(i) != request.user.id:
                event.invite_list.add(i)
        event.save()
        return redirect('/')
    return event_constructor(request, er=1)


def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.user == event.host:
        event.delete()
        return redirect('/')
    return redirect('/')


def update_event(request, event_id):
    if request.method != 'POST':
        return redirect('/')
    event = Event.objects.get(pk=event_id)
    form = ChangeEventForm(request.POST)
    data = request.POST
    if form.is_valid():
        event_time = datetime(
            year=int(data['year']),
            month=int(data['month']),
            day=1,
            hour=int(data['hour']),
            minute=int(data['minute'])
        ) + timedelta(int(data['day']) - 1)
        if event_time < datetime.now():
            return event_editor(request, event.id, er=2)
        event.event_time = event_time
        event.description = data['description']
        event.place = data['place']
        invite = data.getlist('invite_list')
        for i in invite:
            i = int(i)
            if i != request.user.id:
                event.invite_list.add(i)
        invites = event.invite_list.all()
        participants = event.participants.all()
        for i in invites:
            for j in participants:
                if i == j:
                    event.invite_list.remove(i)
        del_partic = data.getlist('delete_participants')
        for i in del_partic:
            i = int(i)
            for j in participants:
                if i == j.id and i != event.host.id:
                    event.participants.remove(i)
        del_inv = data.getlist('delete_invites')
        invites = event.invite_list.all()
        for i in del_inv:
            i = int(i)
            for j in invites:
                if i == j.id:
                    event.invite_list.remove(i)
        event.save()
        return redirect('/event/%s' % (event_id))
    return event_editor(request, event.id, er=1)


def decline_invite(request, event_id):
    event = Event.objects.get(pk=event_id)
    invite_list = event.invite_list.all()
    for i in invite_list:
        if request.user == i:
            event.invite_list.remove(request.user)
            event.save()
            return redirect('/invites')
    return redirect('/')


def accept_invite(request, event_id):
    event = Event.objects.get(pk=event_id)
    invite_list = event.invite_list.all()
    for i in invite_list:
        if request.user == i:
            event.invite_list.remove(request.user)
            event.participants.add(request.user)
            event.save()
            return redirect('/invites')
    return redirect('/')


def leave(request, event_id):
    event = Event.objects.get(pk=event_id)
    participants = event.participants.all()
    for i in participants:
        if request.user == i:
            event.participants.remove(request.user)
            event.save()
    return redirect('/')
