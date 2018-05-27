#imports
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.templatetags.static import static


def index(request):
    imgurl = static('mypage/images/banner.jpg')
    context = {
        'bannerhtml':'<img src="' + imgurl + '" width="100%">'
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context))
    
def fourOfour(request):
    template = loader.get_template('404.html')
    return HttpResponse(template.render())
    
def about(request):
    template = loader.get_template('404.html')
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
    
    
    