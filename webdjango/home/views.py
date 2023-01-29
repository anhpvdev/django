from cgitb import html
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import comic,member
# Create your views here.

def listcomic(request):
    list_comic = comic.objects.all()
    list_member = member.objects.all() 
    return  render(request, 'pages/home.html', {"dscomic": list_comic , "dsmember": list_member})