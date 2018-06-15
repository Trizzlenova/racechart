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
