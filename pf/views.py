# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from wsgiref.util import FileWrapper
import os, tempfile, zipfile
from django.conf import settings
import mimetypes


# Create your views here.

def index(request):

    return render(request, 'base.html') 


def download_zip(request):
    zip_path = root + "A.zip"
    zip_file =  open(zip_path, 'rb')
    response = HttpResponse(zip_file, content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=%s' % 'A.zip'
    response['Content-Length'] = os.path.getsize(zip_path)
    zip_file.close()

    return response
	
	
def send_file(request):


  filename     = "static/ppe1.zip" # Select your file here.
  download_name ="ppe1.zip"
  wrapper      = FileWrapper(open(filename))
  content_type = mimetypes.guess_type(filename)[0]
  response     = HttpResponse(wrapper,content_type=content_type)
  response['Content-Length']      = os.path.getsize(filename)    
  response['Content-Disposition'] = "attachment; filename=%s"%download_name
  return response