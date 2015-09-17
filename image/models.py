from django.db import models
from teams.models import Teams
from match.models import Match
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class Image(models.Model):
    """
    Represents a News. Stores all details of a news
    """
    title = models.CharField(_('title*'), max_length=191)
    image = models.CharField(max_length=200)
    team = models.ForeignKey(Teams,related_name="Team A+",blank=True , null=True)
    tags = models.CharField(_('tags'), max_length=255,blank=True)
    user = models.ForeignKey(User,verbose_name=_('Author'))
    enabled = models.BooleanField(default=True)
    rejected = models.BooleanField(default=False)
    created_date = models.DateTimeField(_('Created Date'), auto_now_add=True)
    modified_date = models.DateTimeField(_('Modified Date'), auto_now=True)
    def __unicode__(self):
        return self.title
    @models.permalink
    def get_absolute_url(self):
    	return ('news_detail', (), {'slug': self.slug, 'news_id': self.id})