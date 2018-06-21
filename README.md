

# Code Highlights
## Initial JSON Grab Code
### 2018-06-12

``` python
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
```
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
```python
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
```

## Seed.py, or, how I learned to love switches

Seeding the database was simple on paper. The API call returns JSON, which Django can turn into a Python dictionary. All the seed.py file had to do was iterate through the JSON, grab the key/value pairs we needed, and toss them into our database. Simple enough.

Unfortunately, not all of the drivers had the keys we wanted. Drivers were missing heights, birthdays, twitter handles, etc... Danica Patrick didn't even have a car. We could leave the values empty, but any attempt to access a non-existent dictionary key threw an error. The data needed to be cleaned.

This was solved by setting up two lists: one with the keys we needed, and another with the keys provided.

```python
wanted_keys = ['name','drivers','actual_distance','avg_speed','caution_laps','cautions','condition','distance','elapsed_time','laps','laps_completed','lead_changes','scheduled_time','start_time','end_time','victory_margin', 'number', 'flags']

provided_keys = list(loaded_race.keys())
keys_to_add = []

```

The lists would be iterated through with a switch that would trigger if a match was found. If no match was found, value would be set to none.

```python
for wanted_key in wanted_keys:
    match_found = False
    for key in provided_keys:
        if wanted_key == key:
            match_found = True
      # if no match is found, add key name to array
    if match_found == False:
        keys_to_add.append(wanted_key)

    # Set missing keys to None
if len(keys_to_add) > 0:
    for key in keys_to_add:
            loaded_race[key] = None
```
### Attaching results to drivers

Results of a race had to be matched to the drivers in our database, which came from the NASCAR 2018 official roster for the Monster Energy Cup, which is the top tier of NASCAR racing. However, there are many leagues, and drivers switch between them, so not all of the drivers listed in a race were on our roster. If we tried iterating through every driver and sending a get request to the database, the function would throw an error if a driver could not be found.

Another switch saved the day.

``` python
for result in results:
# Switch triggers if driver exists in database. This is to avoid No Matching Query error
    driver_binary = len(Driver.objects.filter(full_name=result['driver']['full_name']))
    if driver_binary == 1:
        result['driver'] = Driver.objects.get(full_name=result['driver']['full_name'])
        result['race'] = Race.objects.all()[i]
        result['pit_stops'] = len(result['pit_stops'])
```
Filter returns a list of matching model instances. If a driver was found, that list would contain one element. If not, it would be empty. Therefore, we would only create a result if a driver existed in our database.
