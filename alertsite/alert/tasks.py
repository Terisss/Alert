from celery.decorators import periodic_task
from celery.schedules import crontab
from django.core.mail import send_mass_mail
from .models import Event
import datetime


@periodic_task(run_every=crontab(minute='*/1'))
def play_event():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    filt = datetime.datetime(year, month, day, hour, minute)
    events = Event.objects.filter(event_time=filt)
    for event in events:
        members = event.participants.all()
        to = list()
        for member in members:
            to.append(member.email)
        mail_body = "%s\n\n%s" % (event.place, event.description)
        message = (event.title, mail_body, 'Alertsite', to)
        send_mass_mail((message,), fail_silently=False)
