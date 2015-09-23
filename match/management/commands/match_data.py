from django.core.management.base import BaseCommand
from django.conf import settings
from django.db.models import Count
from django.conf import settings
from django.db import models
import os
import csv
from django.db import transaction
from teams.models import Teams
from match.models import Match
from datetime import datetime

class Command(BaseCommand):
    def handle(self, *args, **options):
        f = open("Delhi-3.csv")
        reader = csv.reader(f)
        date = "2015-10-03"
        slot_type = 1
        j=1
        for row in f.readlines():
            data = row.split('\t')
            if slot_type == 1:
                if data[0] == 'Slot 1':
                    dt = date +", "+"15:30"
                    c = datetime.strptime(str(dt),"%Y-%m-%d, %H:%M")
                    self.save_data(1,data,1,c,date)
                elif data[0] == 'Slot 2':
                    dt = date +", "+"16:10"
                    c = datetime.strptime(str(dt),"%Y-%m-%d, %H:%M")
                    self.save_data(2,data,5,c,date)
                elif data[0] == 'Slot 3':
                    dt = date +", "+"16:50"
                    c = datetime.strptime(str(dt),"%Y-%m-%d, %H:%M")
                    self.save_data(3,data,9,c,date)
                elif data[0] == 'Slot 4':
                    dt = date +", "+"17:30"
                    c = datetime.strptime(str(dt),"%Y-%m-%d, %H:%M")
                    self.save_data(4,data,13,c,date)
                elif data[0] == 'Slot 5':
                    dt = date +", "+"18:10"
                    c = datetime.strptime(str(dt),"%Y-%m-%d, %H:%M")
                    self.save_data(5,data,17,c,date)
                elif data[0] == 'Slot 6':
                    dt = date +", "+"18:50"
                    c = datetime.strptime(str(dt),"%Y-%m-%d, %H:%M")
                    self.save_data(6,data,21,c,date)
                elif data[0] == 'Slot 7':
                    dt = date +", "+"19:30"
                    c = datetime.strptime(str(dt),"%Y-%m-%d, %H:%M")
                    self.save_data(7,data,25,c,date)
                elif data[0] == 'Slot 8':
                    dt = date +", "+"20:10"
                    c = datetime.strptime(str(dt),"%Y-%m-%d, %H:%M")
                    self.save_data(8,data,29,c,date)
                elif data[0] == 'Slot 9':
                    dt = date +", "+"20:50"
                    c = datetime.strptime(str(dt),"%Y-%m-%d, %H:%M")
                    self.save_data(9,data,33,c,date)
                elif data[0] == 'Slot 10':
                    dt = date +", "+"21:30"
                    c = datetime.strptime(str(dt),"%Y-%m-%d, %H:%M")
                    self.save_data(10,data,37,c,date)
            else:
                if data[0] == 'Slot 1':
                    dt = date +", "+"7:00"
                    c = datetime.strptime(str(dt),"%Y-%m-%d, %H:%M")
                    self.save_data(1,data,1,c,date)
                elif data[0] == 'Slot 2':
                    dt = date +", "+"7:40"
                    c = datetime.strptime(str(dt),"%Y-%m-%d, %H:%M")
                    self.save_data(2,data,5,c,date)
                elif data[0] == 'Slot 3':
                    dt = date +", "+"8:20"
                    c = datetime.strptime(str(dt),"%Y-%m-%d, %H:%M")
                    self.save_data(3,data,9,c,date)
                elif data[0] == 'Slot 4':
                    dt = date +", "+"9:00"
                    c = datetime.strptime(str(dt),"%Y-%m-%d, %H:%M")
                    self.save_data(4,data,13,c,date)
                elif data[0] == 'Slot 5':
                    dt = date +", "+"9:40"
                    c = datetime.strptime(str(dt),"%Y-%m-%d, %H:%M")
                    self.save_data(5,data,17,c,date)
                elif data[0] == 'Slot 6':
                    dt = date +", "+"10:20"
                    c = datetime.strptime(str(dt),"%Y-%m-%d, %H:%M")
                    self.save_data(6,data,21,c,date)
                elif data[0] == 'Slot 7':
                    dt = date +", "+"11:00"
                    c = datetime.strptime(str(dt),"%Y-%m-%d, %H:%M")
                    self.save_data(7,data,25,c,date)
                elif data[0] == 'Slot 8':
                    dt = date +", "+"11:40"
                    c = datetime.strptime(str(dt),"%Y-%m-%d, %H:%M")
                    self.save_data(8,data,29,c,date)
                elif data[0] == 'Slot 9':
                    dt = date +", "+"12:20"
                    c = datetime.strptime(str(dt),"%Y-%m-%d, %H:%M")
                    self.save_data(9,data,33,c,date)
                elif data[0] == 'Slot 10':
                    dt = date +", "+"13:00"
                    c = datetime.strptime(str(dt),"%Y-%m-%d, %H:%M")
                    self.save_data(10,data,37,c,date)



    def save_data(self,slot,data,j,c,match_date):
        print data
        city="Delhi"
        slot_type = 1 
        for i in range(2,9,2):
            print "aaaaaaaaa",data[i],data[i+1]
            try:
                team_a = Teams.objects.get(team_name=str(data[i]).replace("\n",""))
                team_b = Teams.objects.get(team_name=str(data[i+1]).replace("\n",""))
            except:
                team_a = None
                team_b = None
            match = Match.objects.create(slot_no=slot,match_no=j,team_a=team_a,team_b=team_b,schedule=c,result_type=1,city=city,match_date=match_date,slot_type=slot_type)
            j=j+1
            print "#########"