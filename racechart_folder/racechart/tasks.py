# to init scheduler, enter: celery -A tasks.celery worker -B -l info

from config import API_KEY
import json
from requests import *
from celery import Celery, chain
import time
from celery.schedules import crontab
from datetime import timedelta

# define how to grab a json from an api:
def grab_json(request, url, data_file):
	response = get(url)
	content = response.content
	data = open(data_file, 'wb')
	data.write(content)
	data.close()
	print(f'you are grabbing a json from {url}')

# define api urls and json file destinations
api = API_KEY
year = '2018'
race_ids = ['cf82b04d-cc9c-4621-aa9b-cbc6ee269de7']

driver_url = f'http://api.sportradar.us/nascar-ot3/mc/{year}/drivers/list.json?api_key={api}'
driver_file = 'json/drivers.json'

standings_url = f'http://api.sportradar.us/nascar-ot3/mc/{year}/standings/drivers.json?api_key={api}'
standings_file = 'json/standings.json'

race_url = f'http://api.sportradar.us/nascar-ot3/mc/races/{race_ids[0]}/results.json?api_key={api}'
race_file = 'json/race.json'

race_list_url = f'http://api.sportradar.us/nascar-t3/mc/{year}/races/schedule.json?api_key={api}'
race_list_file = 'json/race_list.json'

# define a get function for each api source:
def get_driver():
	grab_json(request, driver_url, driver_file)

def get_race():
	i = 0
	grab_json(request, race_url, race_file)

def get_standings():
	grab_json(request, standings_url, standings_file)


# define a get function for multiple races:
def get_all_races():
	grab_json(request, race_list_url, race_list_file)
	race_ids = []
	race_json = open('json/race_list.json').read()
	loaded = json.loads(race_json)
	event_list = loaded['events']
	for events in event_list:
		races = events['races']
		for race in races:
			race_ids.append(race['id'])
	i = 0
	race_url = f'http://api.sportradar.us/nascar-ot3/mc/races/{race_ids[i]}/results.json?api_key={api}'
	length = len(race_ids)
	while(i < 10):
		grab_json(request, race_url, f'json/race_list/race{i}.json')
		print(f'you are grabbing a json from {race_url}')
		time.sleep(3)
		if i > 8:
			print('Grabbed all races!')
			# return HttpResponseRedirect('/admin')
		i = i + 1


celery = Celery(__name__)
celery.config_from_object(__name__)
celery.conf.broker_url = 'redis://localhost:6379'

@celery.task
def ping_me():
	print('celery pinging fmtb')

@celery.task
def access_nascar_api():
	print('Accessing NASCAR API')
	get_driver()
	print('got driver')
	time.sleep(5)
	get_standings()
	print('got standings')
	time.sleep(5)
	get_race()
	print('got race')
	# time.sleep(5)
	# need to add function call to reseed
	# print('Database Updated')

@celery.task
def access_multiple_races():
	get_all_races()

CELERYBEAT_SCHEDULE = {
	'every-twenty-five': {
		'task': 'tasks.ping_me',
		'schedule': timedelta(minutes=25),
	},
	'every-day': {
		'task': 'tasks.access_nascar_api',
		'schedule': crontab(hour=19, minute=28),
		# 'schedule': timedelta(hours=24),
	},
	'twice-montthly': {
		'task': 'tasks.access_nascar_api',
		'schedule': timedelta(hours=350),
	},
}

celery.conf.timezone = 'UTC'
