from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from website.models import News


def index(request):
    latest_news_list = News.objects.exclude(state='0').order_by('-pub_date')[:3]
    template = loader.get_template('website/home.html')
    context = {'latest_news_list': latest_news_list}
    return render(request, 'website/home.html', context)

def about(request):
    return render(request, 'website/about.html', {})

def events(request):
    return render(request, 'website/events.html', {})

def news(request):
    latest_news_list = News.objects.exclude(state='0').order_by('-pub_date')
    paginator = Paginator(latest_news_list, 4)

    page = request.GET.get('page')
    try:
	news = paginator.page(page)
    except PageNotAnInteger:
	news = paginator.page(1)
    except EmptyPage:
	news = paginator.page(paginator.num_pages)    
    return render(request, 'website/news.html', {'news': news})

def newsitem(request, news_id):
    try:
	news = News.objects.exclude(state='0').get(pk=news_id)
    except News.DoesNotExist:
	return render(request, 'website/404.html', {})
    return render(request, 'website/newsitem.html', {'news': news})

def gallery(request):
    return render(request, 'website/gallery.html', {})

def register(request):
    return render(request, 'website/register.html', {})

def contact(request):
    return render(request, 'website/contact.html', {})

def credits(request):
    return render(request, 'website/credits.html', {})

def calendar(request):
    return render(request, 'website/calendar.html', {})
