from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify

# Create your models here.
class Teams(models.Model):
    """
    Represents a Team. Stores all details related to a Teams.
    """
    team_name = models.CharField(max_length=255, unique=True, verbose_name=_('Title* '))
    city = models.CharField(max_length=100,verbose_name=_('City* '))
    team_email = models.CharField(max_length=100, verbose_name=_('email* '),blank=True)
    team_manager = models.CharField(max_length=100, verbose_name=_('team_manager* '),blank=True)
    team_manager_email = models.CharField(max_length=100, verbose_name=_('manager_email'),blank=True)
    team_manager_mob = models.CharField(max_length=100, verbose_name=_('manager_mobileno'),blank=True)
    locality = models.CharField(max_length=100, verbose_name=_('locality'),blank=True)
    fan_count = models.PositiveIntegerField(default=0,editable = False)
    total_points = models.PositiveIntegerField(default=0,editable = False)
    games_played = models.PositiveIntegerField(default=0,editable = False)
    total_goal = models.PositiveIntegerField(default=0,editable = False)
    win = models.PositiveIntegerField(default=0,editable = False)
    draw = models.PositiveIntegerField(default=0,editable = False)
    loss = models.PositiveIntegerField(default=0,editable = False)
    team_group = models.PositiveIntegerField(default=0)
    enabled = models.BooleanField(default=True,help_text='check to enable the team')
    created_date = models.DateTimeField(_('Created Date'), auto_now_add=True)
    modified_date = models.DateTimeField(_('Modified Date'), auto_now=True)

    @models.permalink
    def get_absolute_url(self):
        return ('team_detail', (), {'slug': slugify(self.team_name), 'team_id': self.id})

    def __unicode__(self):
		return self.team_name