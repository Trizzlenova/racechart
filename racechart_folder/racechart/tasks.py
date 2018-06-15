from celery import Celery, chain
from django.utils import timezone
from datetime import timedelta
from django.shortcuts import render
from requests import *
from racechart_folder.config import API_KEY
from collections import OrderedDict

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
driver_file = 'racechart/json/drivers.json'

race_url = f'http://api.sportradar.us/nascar-ot3/mc/races/{race_ids[0]}/results.json?api_key={api}'
race_file = 'racechart/json/race.json'

standings_url = f'http://api.sportradar.us/nascar-ot3/mc/{year}/standings/drivers.json?api_key={api}'
standings_file = 'racechart/json/standings.json'

# define a get function for each api source:
def get_driver(request):
	grab_json(requests, driver_url, driver_file)

def get_race(request):
	grab_json(requests, race_url, race_file)

def get_standings(request):
	grab_json(requests, standings_url, standings_file)

	# return HttpResponseRedirect('/admin')


app = Celery('tasks', broker='amqp://myuser:mypassword@localhost:5672/myvhost')

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
	# Calls test('hello') every 10 seconds.
	sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

	# Calls test('world') every 30 seconds
	sender.add_periodic_task(30.0, test.s('world'), expires=10)

	# Executes every Monday morning at 7:30 a.m.
	sender.add_periodic_task(
		crontab(hour=7, minute=30, day_of_week=1),
		test.s('Happy Mondays!'),
	)

@app.task
def test(arg):
	print(arg)

# app = Celery('tasks', broker='amqp://localhost')

# @periodic_task(run_every=crontab(minute=0, hour='11'))
# def access_nascar_api:
#     chain(get_driver() | get_race() | get_standings())
