from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_POST

from ask.models import Article, Author, Like
from ask.forms import ArticleAdd

def index(request):
    articles = Article.objects.all()
    return render(request, 'ask/index.html', {
        'articles':articles
    })

def add_article(request):
    if request.method == "POST":
        form = ArticleAdd(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main-view'))
    else:
        form = ArticleAdd()

    return render(request, 'ask/add_article.html', {
        'form':form
    })

@require_POST
def like(request):
    try:
        article_id = int(request.POST.get('article_id'))
    except ValueError:
        return JsonResponse({'status': 'error'})
    author = Author.objects.first()

    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        return JsonResponse({'status': 'error'})

    kwargs = {"author": author, "article":article}
    like_qs = Like.objects.filter(**kwargs)
    if like_qs.exists():
        like_qs.delete()
    else:
        Like.objects.create(**kwargs)

    article.count = Like.objects.filter(article=article).count()
    article.save()
    return JsonResponse({
        'status': 'ok',
        'count': article.count
    })

def addlike(request, article_id):
   article = get_object_or_404(Article, id=article_id)  # возвращает id статьи или 404.
   article.article_likes += 1 # Прибавляет единицу к article_likes
   article.save() # сохраняет
   return HttpResponseRedirect('/')
