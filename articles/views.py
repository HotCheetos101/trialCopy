from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Reply
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .import forms
from .forms import ReplyForm


# Create your views here.


def article_list(request):
    articles = Article.objects.all().order_by('date')

    return render(request, 'articles/article_list.html', {'articles': articles})


def article_detail(request, slug):
    # return HttpResponse(slug)
    # article = Article.objects.get(slug=slug)
    # return render(request,'articles/article.detail.html', {'article': article})
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})


def create_reply(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.article = article
            reply.author = request.user
            reply.save()
            return redirect('detail', slug=article.slug)
    else:
        form = ReplyForm()

    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'create_reply.html', context)


@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('list')

    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})
