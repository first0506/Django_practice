from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.views.decorators.http import require_POST

# Create your views here.
def article_list(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/article_list.html', context)

def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form' : form
    }
    return render(request, 'articles/new_article.html', context)

def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/article_detail.html', context)

def update_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update_article.html', context)

@require_POST
def delete_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('articles:index')