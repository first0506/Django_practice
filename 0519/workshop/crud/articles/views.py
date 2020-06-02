from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Article
from .forms import ArticleForm


def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/form.html', context)


def like(request, article_pk):
    user = request.user
    article = get_object_or_404(Article, pk=article_pk)

    if article.like_users.filter(pk=user.pk).exists():
        article.like_users.remove(user)
        # 좋아요 취소
        liked = False
    else:
        article.like_users.add(user)
        # 좋아요 등록
        liked = True

    # return redirect('articles:index')
    return JsonResponse({
        'liked' : liked,
        'like_count' : article.like_users.count(),
    })
