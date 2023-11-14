from django.shortcuts import render,redirect
from .models import Article,Comment
from .forms import ArticleForm,CommentForm
from django.contrib.auth.decorators import login_required

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
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments' : comments,
    }
    
    return render(request, 'prac_app/detail.html', context)

@login_required
def comments_create(request,num):
    article = Article.objects.get(pk=num)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment_form.save()
        return redirect('prac_app:detail', article.pk)
    context = {
        'article' : article,
        'comment_form' : comment_form,
    }
    return render(request, 'prac_app/detail.html',context)

@login_required
def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('prac_app:detail', article_pk)
    
    
    

# def new(reqeust):
#     form = ArticleForm()
#     context = {
#         'form':form,
#     }
#     return render(reqeust,'prac_app/new.html',context)

@login_required
def create(request):
    if request.method == 'POST':
        # 일반 HTML폼/일반 장고폼 사용시 데이터 잡는 방법
        # article = Article(title=request.POST.get('title'), content=request.POST.get('content'))
        # article.save()
        
        # 장고 모델 폼 사용시
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('prac_app:detail', article.pk)
    else:
        form = ArticleForm()
        
    context = {
        'form' : form,
    }
    #유효성 검사 실패시 생성페이지 그대로 유지하기위해 
    #
    return render(request, 'prac_app/create.html', context)
    
@login_required
def delete(request, num):
    article = Article.objects.get(pk=num)
    if request.user == article.user:
        article.delete()
    
    return redirect('prac_app:index')


# def edit(request, num):
#     article = Article.objects.get(pk=num)
#     form = ArticleForm(instance=article)
#     context = {
#         'article': article,
#         'form': form,
#     }
#     return render(request, 'prac_app/edit.html', context)

@login_required
def update(request,num):
    article = Article.objects.get(pk=num)
    if request.user == article.user:
        if request.method == 'POST':
            # 일반 HTML폼 / 혹은 일반 장고폼의 데이터를 잡을 떄 쓰는 방법
            # article.title = request.POST.get('data_title')
            # article.content = request.POST.get('data_content')
            # article.save()
            
            # 모델 장고폼
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('prac_app:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('prac_app:index')
    
    context = {
        'article': article,
        'form' : form,
    }
    return render(request,'prac_app/update.html',context)
    
