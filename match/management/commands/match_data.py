from django.core.management.base import BaseCommand
from django.conf import settings
from django.db.models import Count
from django.conf import settings
from django.db import models
import os
import csv
from django.db import transaction
from teams.models import Teams
from datetime import datetime

class Command(BaseCommand):
    def handle(self, *args, **options):
        f = open("date.txt")
        reader = csv.reader(f)
        date = "2015-09-26"
        j=1
        for row in f.readlines():
            data = row.split('\t')
            if data[0] == 'Slot 1':
                dt = date +", "+"15:30"
                c = datetime.strptime(str(dt),"%Y-%m-%d, %H:%M")
                self.save_data(data,1,c)
            elif data[0] == 'Slot 2':
                dt = date +", "+"16:10"
                c = datetime.strptime(str(dt),"%Y-%m-%d, %H:%M")
                self.save_data(data,5,c)
            elif data[0] == 'Slot 3':
                dt = date +", "+"16:50"
                c = datetime.strptime(str(dt),"%Y-%m-%d, %H:%M")
                self.save_data(data,9,c)
            elif data[0] == 'Slot 4':
                dt = date +", "+"17:30"
                c = datetime.strptime(str(dt),"%Y-%m-%d, %H:%M")
                self.save_data(data,13,c)
            elif data[0] == 'Slot 5':
                dt = date +", "+"18:10"
                c = datetime.strptime(str(dt),"%Y-%m-%d, %H:%M")
                self.save_data(data,17,c)
            elif data[0] == 'Slot 6':
                dt = date +", "+"18:50"
                c = datetime.strptime(str(dt),"%Y-%m-%d, %H:%M")
                self.save_data(data,21,c)
            elif data[0] == 'Slot 7':
                dt = date +", "+"19:30"
                c = datetime.strptime(str(dt),"%Y-%m-%d, %H:%M")
                self.save_data(data,25,c)
            elif data[0] == 'Slot 8':
                dt = date +", "+"20:10"
                c = datetime.strptime(str(dt),"%Y-%m-%d, %H:%M")
                self.save_data(data,29,c)
            elif data[0] == 'Slot 9':
                dt = date +", "+"20:50"
                c = datetime.strptime(str(dt),"%Y-%m-%d, %H:%M")
                self.save_data(data,33,c)
            elif data[0] == 'Slot 10':
                dt = date +", "+"21:30"
                c = datetime.strptime(str(dt),"%Y-%m-%d, %H:%M")
                self.save_data(data,37,c)


    def save_data(self,data,j,c):
        print data
        for i in range(2,9,2):
            team_a = Teams.objects.get(team_name=data[i].replace("\r\n",""))
            team_b = Teams.objects.get(team_name=data[i+1].replace("\r\n",""))
            #match = Match.objects.create(match_no=j,team_a=team_a,team_b=team_b,schedule=c,result_type=1)
            j=j+1
            print "#########"

                
            # team = Teams.objects.create(team_name=team_name,city=team_city,team_email=team_email,team_manager=team_man,team_manager_email=team_man_email,team_manager_mob=team_mob,locality=locality,team_group='2')
            # for i in range(0,10,1):
            #     print i

            #     name = data[i*18+8]
            #     email = data[i*18+9]
                
            #     if data[i*18+10] == "Male":
            #         gendre = '1'
            #     else:
            #         gendre = '2'
            #     mobile_no = data[i*18+11]
            #     address = data[i*18+12]
            #     if (data[i*18+21] != "dummy" and data[i*18+21] != ""):
            #         image = os.path.join(settings.MEDIA_URL, (data[i*18+21]+".jpg"))
            #     else:
            #         image = None
            #     print name,email,gendre,mobile_no,address,image
            #     print "**********************************"
            #     player = Player.objects.create(name=name,team=team,email=email,gendre=gendre,mobile_no=mobile_no,address=address,image=image,team_group='2')