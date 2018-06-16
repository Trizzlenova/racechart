# Initial JSON Grab Code
## 2018-06-12

def grab_json(requests, url, data_file):
  response = get(url)
  content = response.content
  data = open(data_file, 'wb')
  data.write(content)
  data.close()
  print(f'you are grabbing a json from {url}')

def get_all(requests):
  grab_json(requests, driver_url, driver_file)
  grab_json(requests, race_url, race_file)
  return HttpResponseRedirect('/admin')

## 2018-06-13
def create_driver(request):
  driver_json = open('racechart/json/drivers.json').read()
  loaded = json.loads(driver_json)
  print(loaded['drivers'][0]['full_name'])
  birthday = loaded['drivers'][0]['birthday']
  full_name = loaded['drivers'][0]['full_name']
  country = loaded['drivers'][0]['country']
  birth_place = loaded['drivers'][0]['birth_place']

  david_ragan = Driver.create(full_name, birth_place, birthday, country)
  david_ragan.save()
  print(david_ragan)

  return HttpResponseRedirect('/admin')


# Scheduling the JSON Grab
## 2018-06-16

@celery.task
def access_nascar_api():
	print('Accessing NASCAR API')
	get_race()
	print('got race')
	time.sleep(5)
	get_driver()
	print('got driver')
	time.sleep(5)
	get_standings()
	print('got standings')
	# time.sleep(5)
	# need to add function call to reseed
	# print('Database Updated')

CELERYBEAT_SCHEDULE = {
    'every-second': {
        'task': 'tasks.access_nascar_api',
		'schedule': crontab(hour=19, minute=28),
    },
}

celery.conf.timezone = 'UTC'
