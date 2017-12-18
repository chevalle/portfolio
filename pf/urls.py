from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^parcours/', views.parcours, name='parcours'),
    url(r'^competences/', views.competences, name='competences'),
    url(r'^projets/', views.projets, name='projets'),
    url(r'^contact/', views.contact, name='contact'),
	url(r'^eng/home$', views.index_eng, name='eng'),
	url(r'^eng/background', views.background, name='background'),
	url(r'^eng/projects', views.projects, name='projects'),
	url(r'^eng/skills', views.skills, name='skills'),
	url(r'^eng/contact', views.contact_eng, name='contact-eng'),
	url(r'^static/ppe1.zip', views.send_file)
	
]
