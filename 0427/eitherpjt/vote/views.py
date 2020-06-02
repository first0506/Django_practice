from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Vote, Comment
from .forms import VoteForm, CommentForm

# Create your views here.
def create(request):
    if request.method=='POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            vote = form.save()
            return redirect('vote:detail', vote.pk)
    else:
        form = VoteForm()
    context = {
        'form' : form
    }
    return render(request, 'vote/form.html', context)

def index(request):
    votes = Vote.objects.order_by('-pk')
    context = {
        'votes' : votes
    }
    return render(request, 'vote/index.html', context)

def detail(request, vote_pk):
    vote = get_object_or_404(Vote, pk=vote_pk)
    form = CommentForm()
    total = vote.a_cnt+vote.b_cnt
    if total:
        a_percent = int((vote.a_cnt/total)*100)
        b_percent = 100-a_percent
    else:
        a_percent = 50
        b_percent = 50
    context = {
        'vote' : vote,
        'form' : form,
        'total' : total,
        'a_percent' : a_percent,
        'b_percent' : b_percent,
    }
    return render(request, 'vote/detail.html', context)

@require_POST
def comments_create(request, vote_pk):
    vote = get_object_or_404(Vote, pk=vote_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.vote = vote
        comment.save()
        if comment.votes=='LEFT':
            vote.a_cnt += 1
        else:
            vote.b_cnt += 1
        vote.save()
    return redirect('vote:detail', vote.pk)

def random(request):
    if Vote.objects.all():
        vote = Vote.objects.order_by('?').first()
        return redirect('vote:detail', vote.pk)
    else:
        votes = Vote.objects.order_by('-pk')
        context = {
            'votes' : votes
        }
        return render(request, 'vote/index.html', context)