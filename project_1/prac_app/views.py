from django.shortcuts import render,redirect
from .models import Article
import random

# Create your views here.


def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'prac_app/index.html',context)


def detail(request,num):
    article = Article.objects.get(pk=num)
    
    context = {
        'article': article,
    }
    
    return render(request, 'prac_app/detail.html', context)
    

def new(reqeust):
    return render(reqeust,'prac_app/new.html')


def create(request):
    article = Article(title=request.POST.get('input_title'), content=request.POST.get('input_content'))
    article.save()
    
    return redirect('prac_app:detail', article.pk)


def delete(request, num):
    article = Article.objects.get(pk=num)
    article.delete()
    
    return redirect('prac_app:index')


def edit(request, num):
    article = Article.objects.get(pk=num)
    context = {
        'article': article,
    }
    return render(request, 'prac_app/edit.html', context)


def update(request,num):
    article = Article.objects.get(pk=num)
    article.title = request.POST.get('data_title')
    article.content = request.POST.get('data_content')
    article.save()
    
    return redirect('prac_app:detail', article.pk)


