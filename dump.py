import csv
from teams.models import Teams
f = open("test.csv")
reader = csv.reader(f)
for row in f.readlines():
	data = row.split(',')
	team_name = data[0]
	team_city = data[1]
	team_email = data[2]
	team_man = data[3]
	team_man_email = data[4]
	team_mob = data[5]
	locality = data[6]
	team = Teams.objects.get(team_name=team_name,city=team_city,team_email=team_email,team_manager=team_man,team_manager_email=team_man_email,team_manager_mob=team_mob,locality=locality,team_group='1')
	print team_name,team_city,team_email,team_man,team_mob,locality
	
	break