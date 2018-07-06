#imports
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.templatetags.static import static
from django.contrib import admin
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required


def index(request):
    imgurl = static('mypage/images/banner.jpg')
    context = {
        'bannerhtml':'<img src="' + imgurl + '" width="100%">'
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context))
    
def snake(request):
    template = loader.get_template('snake.html')
    return HttpResponse(template.render())
    
def fourOfour(request):
    template = loader.get_template('404.html')
    return HttpResponse(template.render())
    
def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())
    
def contact(request):
    template = loader.get_template('404.html')
    return HttpResponse(template.render())
    
def projects(request):
    template = loader.get_template('404.html')
    return HttpResponse(template.render())
    
def art(request):
    template = loader.get_template('404.html')
    return HttpResponse(template.render())
    
def pso(request):
    template = loader.get_template('pso.html')
    return HttpResponse(template.render())
    
@login_required(login_url='/admin/')
def makePostPage(request):
    template = loader.get_template('makePost.html')
    return HttpResponse(template.render())
    
    
    