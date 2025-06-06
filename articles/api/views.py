from django.shortcuts import render, redirect
from articles.models import Article
from django.db.models import Q

def index(request):
    query = request.GET.get('q', '')
    if query:
        articles = Article.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    else:
        articles = Article.objects.all()
    return render(request, 'articles/index.html', {'articles': articles, 'query': query})

def add_article(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            Article.objects.create(title=title, content=content)
            return redirect('index')
    return render(request, 'articles/add.html')

def agb(request):
    return render(request, 'articles/agb.html')

def legal_notice(request):
    return render(request, 'articles/legal_notice.html')
