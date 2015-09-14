from django.contrib import admin
from teams.models import Teams
from django.conf import settings


class TeamAdmin(admin.ModelAdmin):
    list_display = ("team_name","team_manager")
admin.site.register(Teams,TeamAdmin)
