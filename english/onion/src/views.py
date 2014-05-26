#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response, redirect
from django.template import Template, RequestContext
import json
import re
import word_level
from conf import *
from utils import *
from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField()

#def read(request, pk):
def read(request):
    txt = word_level.api()
    return render_to_response('read.html', {'title':'article', 'txt':txt})

def fit_urlpath(fname):
    return re.match('^[\w\.]+$', fname)
    
def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if not form.is_valid():
            return HttpResponseBadRequest()
        f = request.FILES['file']
        if not fit_urlpath(f.name):
            return HttpResponseBadRequest('file name should only contaions alpha, num, or _')
        elif f.size > UPLOAD_LIMIT:
            return HttpResponseBadRequest('file size too big: ' + str(f.size))
        else:
            return process(request, f.name, f.read())
    else:
        return render_to_response('upload.html', {'form': UploadFileForm}, 
                    context_instance=RequestContext(request))

@benchmark
def upload_txt(request):
    if not request.method == 'POST':
        return HttpResponseBadRequest()
    data = request.POST.get('content', '')
    test_name = request.POST.get('test_name', '')
    if not data.strip():
        return HttpResponseBadRequest(data)
    elif not test_name or not fit_urlpath(test_name):
            return HttpResponseBadRequest('file name should only contaions alpha, num, or _')
    elif len(data) > UPLOAD_LIMIT:
        return HttpResponseBadRequest('Error: file size too big: ' + len(data))        
    else:
        return process(request, test_name, tounicode(data))
    
def json_response(dic):
    json_response = json.dumps(dic)
    return HttpResponse(json_response, mimetype='application/json')
    
@benchmark
def process(request, fname, data):
    word_level.set_txt(data)
    return redirect(request.path.rsplit('/', 1)[0]+'/') 

#@benchmark
def word_mark(request):
    w, unkown = [request.POST.get(i, '') for i in ('w', 'unkown')]
    unkown = unkown == 'true' and True or False
    if w:
        txt = word_level.updateK(w, unkown)
        return json_response({'txt':txt})