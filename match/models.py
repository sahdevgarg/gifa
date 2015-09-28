from django.db import models
from teams.models import Teams
import datetime
from gifa.gifa_constant import *
from django.utils.translation import ugettext_lazy as _

team_list = ((0,'None'),(1,'team_a'),(2,'team_b'))
class Match(models.Model):
	"""
	Represents a Match. Stores all details related to a Match.
	"""
	match_no = models.PositiveIntegerField(unique=False,blank=False,verbose_name=_('Match no* '))
	team_a = models.ForeignKey(Teams,related_name="Team A+",null=True,blank=True)
	team_b = models.ForeignKey(Teams,related_name="Team B+",null=True,blank=True)
	venue = models.CharField(max_length=255, blank=True)
	city = models.CharField(max_length=190, blank=False)
	schedule = models.DateField(_("match Date time"))
	match_date = models.DateField(_("Match Date"))
	result_type = models.IntegerField( choices=RESULT_LIST_TYPES, blank=False, null=False, verbose_name=_('result type*'),help_text=_("Result Type type 1:match scheduled, 2: match with result,3: match with draw,4: match canceled,5: walkover"))
	team_a_goal = models.IntegerField(_('Team A Goal'),default=0)
	slot_type = models.IntegerField(_('slot_type'),default=1)
	schedule =  models.DateTimeField(_('Scheduled Date'))
	team_b_goal = models.IntegerField(_('Team B Goal'),default=0)
	winning_team = models.ForeignKey(Teams,null=True,related_name="Winning Team+",editable = False)
	walkover = models.IntegerField( choices=team_list,default=0, verbose_name=_('walkover'))
	slot_no = models.IntegerField( choices=SOLT_NO, blank=False, null=False, verbose_name=_('slot_no*'))
	created_date = models.DateTimeField(_('Created Date'), auto_now_add=True)
	modified_date = models.DateTimeField(_('Modified Date'), auto_now=True)
	enabled = models.BooleanField(default=True,help_text='check to enable the Match')
