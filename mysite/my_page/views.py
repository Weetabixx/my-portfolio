#imports
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.templatetags.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.template import RequestContext

from .forms import PostForm

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
    if request.method != 'POST':
        form = PostForm()
        context = {'form' : form}
        template = loader.get_template('makePost.html')
        return render(request, 'makePost.html', context)
        #return HttpResponse(template.render(context))
    # create a form instance and populate it with data from the request:
    form = PostForm(request.POST)
    # check whether it's valid:
    if form.is_valid():
        # process the data in form.cleaned_data as required
        post_type = form.cleaned_data['post_type']
        post_title = form.cleaned_data['post_title']
        post_html_text = form.cleaned_data['post_html_text']
        post_description = form.cleaned_data['post_description']
        post_confirm = form.cleaned_data['post_confirm']
        
        if not post_confirm:
            form.post_confirm = True
            context = {
                'form' : form,
                'post_title': post_title,
                'post_html_text': post_html_text
            }
            template = loader.get_template('previewPost.html')
            return render(request, 'previewPost.html', context)
            
        # redirect to a new URL:
        return HttpResponseRedirect('/')

    
    