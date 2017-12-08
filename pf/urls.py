from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^parcours/', views.parcours, name='parcours'),
    url(r'^competences/', views.competences, name='competences'),
    url(r'^projets/', views.projets, name='projets'),
    url(r'^contact/', views.contact, name='contact'),
]
