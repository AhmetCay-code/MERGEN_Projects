from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path("", views.index, name='index'),
    path("sections1/<int:num>", views.section1, name='section1'),
    path("sections2/<int:num>", views.section2, name='section2'),
    path("sections3/<int:num>", views.section3, name='section3'),
    path("sections4/<int:num>", views.section4, name='section4'),
    path("sections5/<int:num>", views.section5, name='section5'),
    path("favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
    ),
]

urlpatterns += staticfiles_urlpatterns()