from django.db import models
from teams.models import Teams
from django.utils.translation import ugettext_lazy as _


class Player(models.Model):
	"""
	Represents a player. Stores all details related to a player.
	"""
	name = models.CharField(max_length=255, verbose_name=_('name* '))
	team = models.ForeignKey(Teams)
	email = models.CharField(max_length=150,blank=True)	
	fan_count = models.PositiveIntegerField(default=0)
	games_played = models.PositiveIntegerField(default=0)
	total_goal = models.PositiveIntegerField(default=0)
	gendre = models.PositiveIntegerField(default=1)
	mobile_no = models.CharField(max_length=150)
	address = models.CharField(max_length=255 , blank=True)
	team_group = models.PositiveIntegerField(default=0,editable = False)
	image = models.CharField(max_length=200, blank=True,null=True)
	enabled = models.BooleanField(default=True)
	created_date = models.DateTimeField(_('Created Date'), auto_now_add=True)
	modified_date = models.DateTimeField(_('Modified Date'), auto_now=True)

	def __unicode__(self):
		return self.name
# Create your models here.
