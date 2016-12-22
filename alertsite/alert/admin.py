from django.contrib import admin

from .models import Event
# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'host',
        'title',
        'description',
        'creation_date',
        'event_time',
        'is_active'
    )
    list_filter = ['host']

admin.site.register(Event, EventAdmin)
