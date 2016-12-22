from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
import views


urlpatterns = [
    url(r'^([0-9]+)/$', views.create_comments, name='create_comments'),
    url(r'^([0-9]+)/update$', views.update_comment, name='update_comments'),
    url(r'^([0-9]+)/delete$', views.del_comments, name='del_comments'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
