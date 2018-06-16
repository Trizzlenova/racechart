from django.shortcuts import render
from requests import *
from .models import Driver
import json
from django.http import HttpResponse, HttpResponseRedirect
from racechart_folder.config import API_KEY


api = API_KEY
year = '2018'
race_ids = ['cf82b04d-cc9c-4621-aa9b-cbc6ee269de7', 'bf77ec20-2737-4adf-9442-aea6bf8e55a2']

driver_url = f'http://api.sportradar.us/nascar-ot3/mc/{year}/drivers/list.json?api_key={api}'
driver_file = 'racechart/json/drivers.json'

race_url = f'http://api.sportradar.us/nascar-ot3/mc/races/{race_ids[1]}/results.json?api_key={api}'
race_file = 'racechart/json/race.json'

standings_url = f'http://api.sportradar.us/nascar-ot3/mc/{year}/standings/drivers.json?api_key={api}'
standings_file = 'racechart/json/standings.json'

def see_css(request):
    return render(request, 'racechart/driver_list.html')

def grab_json(request, url, data_file):
  response = get(url)
  content = response.content
  data = open(data_file, 'wb')
  data.write(content)
  data.close()
  print(f'you are grabbing a json from {url}')

def get_all(request):
  # grab_json(request, driver_url, driver_file)
  grab_json(request, race_url, race_file)
  # grab_json(request, standings_url, standings_file)
  return HttpResponseRedirect('/admin')

def create_driver(request):
  driver_json = open('racechart/json/drivers.json').read()
  loaded = json.loads(driver_json)
  print(loaded['drivers'][0]['full_name'])
  birthday = loaded['drivers'][0]['birthday']
  full_name = loaded['drivers'][0]['full_name']
  country = loaded['drivers'][0]['country']
  birth_place = loaded['drivers'][0]['birth_place']

  # david_ragan = Driver.create(full_name, birth_place, birthday, country)
  # david_ragan.save()
  # print(david_ragan)

  return HttpResponseRedirect('/admin')
