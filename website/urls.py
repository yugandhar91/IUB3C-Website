from django.conf.urls import patterns, url

from website import views

urlpatterns = patterns('',
    url(r'^$', views.index, name="index"),
    url(r'^about/$', views.about, name="about"),
    url(r'^events/$', views.events, name="events"),
    url(r'^news/$', views.news, name="news"),
    url(r'^news/(?P<news_id>\d+)/$', views.newsitem, name="newsitem"),
    url(r'^gallery/$', views.gallery, name="gallery"),
    url(r'^register/$', views.register, name="register"),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^credits/$', views.credits, name="credits"),
    url(r'^calendar/$', views.calendar, name="calendar"),
)
