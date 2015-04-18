from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'iu3c.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('website.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
