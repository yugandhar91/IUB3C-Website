from django.contrib import admin
from website.models import News

class NewsAdmin(admin.ModelAdmin):
    fields = ['news_title', 'news_body', 'flickr', 'pub_date', 'state']
    list_display = ('news_title', 'pub_date', 'is_published')
    list_filter = ['state']
    search_fields = ['news_title']

admin.site.site_header = "IU Chinese Calligraphy Club"
admin.site.register(News, NewsAdmin)
