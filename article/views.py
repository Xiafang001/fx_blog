from django.shortcuts import render
from article.models import Article, Tag, Classification
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.contrib.syndication.views import Feed
from django.core import serializers
from article.forms import SayHelloForm
from django import forms
import json


# Create your views here.
def home(request):
    is_home = True
    articles = Article.objects.all()
    paginator = Paginator(articles, 6)
    page_num = request.GET.get('page')
    try:
        articles = paginator.page(page_num)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    classification = Classification.class_list.get_Class_list()
    tagCloud = json.dumps(Tag.tag_list.get_Tag_list(), ensure_ascii=False)
    date_list = Article.date_list.get_Article_onDate()

    return render(request, 'blog/index.html', locals())


def detail(request, year, month, day, id):
    try:
        article = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    classification = Classification.class_list.get_Class_list()
    tagCloud = json.dumps(Tag.tag_list.get_Tag_list(), ensure_ascii=False)
    date_list = Article.date_list.get_Article_onDate()
    return render(request, 'blog/content.html', locals())


def archive_month(request, year, month):
    is_arch_month = True
    articles = Article.objects.filter(publish_time__year=year).filter(publish_time__month=month)
    paginator = Paginator(articles, 6)
    page_num = request.GET.get('page')
    try:
        articles = paginator.page(page_num)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    classification = Classification.class_list.get_Class_list()
    tagCloud = json.dumps(Tag.tag_list.get_Tag_list(), ensure_ascii=False)
    date_list = Article.date_list.get_Article_onDate()
    return render(request, 'blog/index.html', locals())


def classfiDetail(request, classfi):
    is_classfi = True
    temp = Classification.objects.get(name=classfi)
    articles = temp.article_set.all()
    paginator = Paginator(articles, 6)
    page_num = request.GET.get('page')
    try:
        articles = paginator.page(page_num)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    classification = Classification.class_list.get_Class_list()
    tagCloud = json.dumps(Tag.tag_list.get_Tag_list(), ensure_ascii=False)
    date_list = Article.date_list.get_Article_onDate()
    return render(request, 'blog/index.html', locals())


def tagDetail(request, tag):
    is_tag = True
    temp = Tag.objects.get(name=tag)
    articles = temp.article_set.all()
    paginator = Paginator(articles, 6)
    page_num = request.GET.get('page')
    try:
        articles = paginator.page(page_num)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    classification = Classification.class_list.get_Class_list()
    tagCloud = json.dumps(Tag.tag_list.get_Tag_list(), ensure_ascii=False)
    date_list = Article.date_list.get_Article_onDate()
    return render(request, 'blog/index.html', locals())


def about(request):
    classification = Classification.class_list.get_Class_list()
    tagCloud = json.dumps(Tag.tag_list.get_Tag_list(), ensure_ascii=False)
    date_list = Article.date_list.get_Article_onDate()
    return render(request, 'blog/about.html', locals())


def archive(request):
    archive = Article.date_list.get_Article_OnArchive()
    ar_newpost = Article.objects.order_by('-publish_time')[:10]
    classification = Classification.class_list.get_Class_list()
    tagCloud = json.dumps(Tag.tag_list.get_Tag_list(), ensure_ascii=False)
    date_list = Article.date_list.get_Article_onDate()
    return render(request, 'blog/archive.html', locals())


class RSSFeed(Feed):
    title = "RSS feed - F's blog"
    link = "feeds/posts/"
    description = "RSS feed - blog posts"

    def items(self):
        return Article.objects.order_by('-publish_time')

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.publish_time

    def item_description(self, item):
        return item.content


def blog_search(request):

    is_search = True
    classification = Classification.class_list.get_Class_list()
    tagCloud = json.dumps(Tag.tag_list.get_Tag_list(), ensure_ascii=False)
    date_list = Article.date_list.get_Article_onDate()
    error = False
    if 's'in request.GET:
        s = request.GET['s']
        if not s:
            return render(request, 'blog/index.html')
        else:
            articles = Article.objects.filter(title__icontains=s)
            if len(articles) == 0:
                error = True
    return render(request, 'blog/index.html', locals())


def message(request): 
    classification = Classification.class_list.get_Class_list()
    tagCloud = json.dumps(Tag.tag_list.get_Tag_list(), ensure_ascii=False)
    date_list = Article.date_list.get_Article_onDate()
    if request.method == "POST":
        form = SayHelloForm(request.POST)
        if form.is_valid():
            form.save()
            name = request.POST['name']
            return render(request, 'blog/thanks.html', locals()) 
        return render(request, 'blog/message.html', locals())
    else:
        form = SayHelloForm()
        return render(request, 'blog/message.html', locals())
