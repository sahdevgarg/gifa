from django.core.management.base import BaseCommand
from django.conf import settings
from django.db.models import Count
from django.conf import settings
import os
from django.db import transaction
import csv
from teams.models import Teams
from match.models import Match
from player.models import Player
class Command(BaseCommand):
    def handle(self, *args, **options):
        f = open("Gurgaon-junior.csv")
        reader = csv.reader(f)
        for row in f.readlines():
            data = row.split('\t')
            team_name = data[0]
            team_city = data[1]
            team_email = data[2]
            team_man = data[3]
            team_man_email = data[4]
            team_mob = data[5]
            locality = data[6]
            try:
                if team_name:
                    team = Teams.objects.create(team_name=team_name,city=team_city,team_email=team_email,team_manager=team_man,team_manager_email=team_man_email,team_manager_mob=team_mob,locality=locality,team_group='2')
                else:
                    pass
            except:
                pass
            for i in range(0,10,1):
                print i

                name = data[i*18+8]
                email = data[i*18+9]
                
                if data[i*18+10] == "Male":
                    gendre = '1'
                else:
                    gendre = '2'
                mobile_no = data[i*18+11]
                address = data[i*18+12]
                if (data[i*18+21] != "dummy" and data[i*18+21] != ""):
                    image = os.path.join(settings.MEDIA_URL, (data[i*18+21]+".jpg"))
                else:
                    image = None
                print name,email,gendre,mobile_no,address,image
                print "**********************************"
                try:
                    player = Player.objects.create(name=name,team=team,email=email,gendre=gendre,mobile_no=mobile_no,address=address,image=image,team_group='2')
                except:
                    pass