from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class Contact(models.Model):
    """
    Represents a News. Stores all details of a news
    """
    title = models.CharField(_('title*'), max_length=191)
    message = models.TextField(blank=True)
    email = models.CharField(_('tags'), max_length=255,blank=True)
    resolved = models.BooleanField(default=False)
    created_date = models.DateTimeField(_('Created Date'), auto_now_add=True)
    modified_date = models.DateTimeField(_('Modified Date'), auto_now=True)


    def __unicode__(self):
        return self.title
   