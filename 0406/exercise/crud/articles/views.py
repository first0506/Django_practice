from django.shortcuts import render
from .models import Article
from django.shortcuts import redirect

# Create your views here.
def article_list(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/article_list.html', context)

def new_article(request):
    return render(request, 'articles/new_article.html')

def create_article(request):
    article = Article()
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)

def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/article_detail.html', context)

def edit_article(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article
    }
    return render(request, 'articles/edit_article.html', context)


def update_article(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)

def delete_article(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('articles:index')