from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def call_login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def call_main(request):
    template = loader.get_template('main_page.html')
    return HttpResponse(template.render())