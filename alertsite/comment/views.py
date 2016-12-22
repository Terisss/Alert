from django.shortcuts import redirect

from .forms import CommentsForm
from .models import Comment
from alert.models import Event
# Create your views here.


def create_comments(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = CommentsForm(request.POST)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.event = event
        obj.author = request.user
        obj.save()
        return redirect('/event/%s#comments' % event.id)
    return redirect('/')


def del_comments(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    event = comment.event
    if request.user == comment.author:
        comment.delete()
        return redirect('/event/%s#comments' % event.id)
    return redirect('/')


def update_comment(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    event = comment.event.id
    form = CommentsForm(request.POST)
    if form.is_valid():
        comment.body = request.POST['body']
        comment.save()
        return redirect('/event/%s#comments' % event)
    return redirect('/')
