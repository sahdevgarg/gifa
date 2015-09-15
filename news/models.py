from django.db import models
from teams.models import Teams
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class News(models.Model):
    """
    Represents a News. Stores all details of a news
    """
    user = models.ForeignKey(User,verbose_name=_('Author'))
    title = models.CharField(_('title*'), max_length=191)
    slug = models.SlugField(max_length=191, unique=True)
    content = models.TextField(blank=True, help_text=_("1: Styling should not be applied on empty paragraphs and para containing image or iframe.<br/> 2: Font Size -> Bold behaves different from Bold -> Font Size (First apply size then bold)"))
    coverimage = models.CharField(max_length=200)
    team_a = models.ForeignKey(Teams,related_name="Team A+")
    # comment_count = models.PositiveIntegerField(default=0,editable = False)
    team_b = models.ForeignKey(Teams,related_name="Team B+",null=True,blank=True)
    tags = models.CharField(_('tags'), max_length=255,blank=True)
    seo_desc = models.TextField(blank=True)
    enabled = models.BooleanField(default=True)
    created_date = models.DateTimeField(_('Created Date'), auto_now_add=True)
    modified_date = models.DateTimeField(_('Modified Date'), auto_now=True)
    def __unicode__(self):
        return self.title
    @models.permalink
    def get_absolute_url(self):
    	return ('news_detail', (), {'slug': self.slug, 'news_id': self.id})

class FeaturedNews(models.Model):
    faetured_news = models.ForeignKey('News');
    enabled = models.BooleanField(default=True)
    created_date = models.DateTimeField(_('Created Date'), auto_now_add=True)
    modified_date = models.DateTimeField(_('Modified Date'), auto_now=True)


