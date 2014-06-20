#coding: utf8

import json
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response, redirect
from django.template import Template, RequestContext
from django import forms
from captcha.fields import CaptchaField 
import word_level
from conf import *
from utils import *


pagesize=6000


def read(request):
    uid = request.user.id
    if request.method == 'GET':
        return render_to_response('read.html', context_instance=RequestContext(request))
    elif request.method == 'POST':
        fname, txt = [request.POST.get(i, '') for i in ('fname', 'txt')]
        assert len(txt) < pagesize
        dic = {'title':fname,
             'article': article_html(word_level.decorate(to_lines(txt), uid)),
             }     
        return json_response(dic)


def article_html(lines):
    res = ''
    for line in lines:
        res +="<p class='p_txt'>%s</p>" %line
    return res

def unknown_word_html(dic):
    res=''
    for k,v in dic.iteritems():
        res += "<div><span class='unknown_word wl_%s'>%s</span> " %(v[2], k) +\
            "<span class='dt'>%s</span></div><div>%s</div>" %(v[1], v[0])
    return res

def json_response(dic):
    json_response = json.dumps(dic)
    return HttpResponse(json_response, mimetype='application/json')


def word_mark(request):
    uid = request.user.id
    w, unknown, txt = [request.POST.get(i, '') for i in ('w', 'unknown', 'txt')]
    w = w.strip()
    unknown = unknown == 'true' and True or False
    if w:
        lines = list(word_level.updateK(w.strip(), unknown, txt, uid))
        return json_response({'lines': lines})


Myword_type={0:'known', 1:'unkown', -1:'forgotten'}

def word_known(request):
    return mywords(request, 0)

def word_unknown(request):
    return mywords(request, 1)

def word_forgotten(request):
    return mywords(request, -1)

def mywords(request, wtype):
    return render_to_response('mywords.html', 
            {'title': Myword_type.get(wtype,0), 
            'dic': word_level.mywords(request.user.id, wtype)
            },
            context_instance=RequestContext(request))

def word_save(request):
    uid = request.user.id
    if not request.method == 'POST':
        return HttpResponseBadRequest()
    w = request.POST.get('w').strip()
    if w:
        word_level.save(w, uid)
    return redirect('/word_forgottern')

def word_repeat(request):
    uid = request.user.id
    if not request.method == 'POST':
        return HttpResponseBadRequest()
    w = request.POST.get('w').strip()
    if w:
        word_level.repeat(w, uid)
    return json_response({'wait': word_level.time2wait(uid),
                         'unknown': unknown_word_html(dict(word_level.show_unknowns(uid))),
                         })
