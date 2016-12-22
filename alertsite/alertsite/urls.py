"""alertsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^invites/$', views.invites, name='invites'),
    url(r'^not_active/$', views.not_active, name='not_active'),
    url(r'^reg_auth/$', views.reg_auth, name='reg_auth'),
    url(r'^reg/$', views.registration, name='reg'),
    url(r'^create_user/$', views.create_user, name='create_user'),
    url(r'^auth/$', views.authentification, name='auth'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^user/$', views.user, name='user'),
    url(r'^update_user/', views.update_user, name='update_user'),
    url(r'^event/', include('alert.urls')),
    url(r'^comment/', include('comment.urls')),
    url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
