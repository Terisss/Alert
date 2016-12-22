from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
import views


urlpatterns = [
    url(r'^$', views.event_constructor, name='event_constructor'),
    url(r'^([0-9]+)/$', views.event, name='event'),
    url(r'^([0-9]+)/edit/$', views.event_editor, name='event_editor'),
    url(r'^([0-9]+)/decline/$', views.decline_invite, name='decline'),
    url(r'^([0-9]+)/accept/$', views.accept_invite, name='accept'),
    url(r'^([0-9]+)/leave/$', views.leave, name='leave'),
    url(r'^([0-9]+)/delete/$', views.delete_event, name='delete_event'),
    url(r'^([0-9]+)/update/$', views.update_event, name='update_event'),
    url(r'^create_event/$', views.create_event, name='create_event'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
