from django.db import models
from ckeditor.fields import RichTextField

# Defining the database table and the columns in it
class News(models.Model):
    # Max length of title field is set to 150
    # I don't think anyone will write a title that long :)
    published = '1'
    draft = '0'
    news_state_choices = (
	(published, 'Published'),
	(draft, 'Draft'),
    )
    news_title = models.CharField(max_length=150)
    news_body = RichTextField('news content', blank=True)
    pub_date = models.DateTimeField('date published')
    flickr = models.CharField(max_length=50, default='0')
    state = models.CharField(max_length=1, choices=news_state_choices, default=draft)

    def __str__(self):
	return self.news_title

    def is_published(self):
	return self.state == '1'
    
    is_published.admin_order_field = 'state'
    is_published.boolean = True
    is_published.short_description = "Published?"
