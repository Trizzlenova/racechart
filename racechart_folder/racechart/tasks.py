# to init, enter: celery -A tasks.celery worker -B -l info
from celery import Celery, chain, group
from config import API_KEY
from datetime import timedelta


# define how to grab a json from an api:
def grab_json(url, data_file):
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
def get_driver():
	grab_json(driver_url, driver_file)

def get_race():
	grab_json(race_url, race_file)

def get_standings():
	grab_json(standings_url, standings_file)


celery = Celery(__name__)
celery.config_from_object(__name__)
celery.conf.broker_url = 'redis://localhost:6379'

@celery.task
def access_nascar_api():
	print('Accessed NASCAR API')
	chain(get_driver() | get_race() | get_standings())


CELERYBEAT_SCHEDULE = {
    'every-second': {
        'task': 'tasks.access_nascar_api',
        'schedule': timedelta(seconds=30),
    },
}
