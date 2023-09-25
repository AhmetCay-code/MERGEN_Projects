from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path("", views.render, name='index'),
    path("stats/", views.stats, name='stats'),
]

urlpatterns += staticfiles_urlpatterns()