# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from wsgiref.util import FileWrapper
import os

# Create your views here.

def index(request):

    return render(request, 'index.html') 

def parcours(request): 
 
    return render(request, 'parcours.html') 

def competences(request):

    return render(request, 'competences.html')

def contact(request):

    return render(request, 'contact.html')

def projets(request): 
 
    return render(request, 'projets.html')

def send_file(request):

    filename = __file__ # Select your file here.                                
    wrapper = FileWrapper(file(filename))
    response = HttpResponse(wrapper, content_type='text/plain')
    response['Content-Length'] = os.path.getsize(filename)
    return response
