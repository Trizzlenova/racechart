from django.shortcuts import render
from requests import *
import json
from django.http import HttpResponse, HttpResponseRedirect
from racechart_folder.config import API_KEY

drivers = []

def get_drivers(requests):
  # hide key before pushing to git
  api = API_KEY
  url = f'http://api.sportradar.us/nascar-ot3/mc/2018/drivers/list.json?api_key={api}'
  response = get(url)
  content = response.content
  data = open('racechart/json/drivers.json', 'wb')
  data.write(content)
  data.close()
  return HttpResponseRedirect('/admin')

  # parsed = json.loads(response.content

  # drivers = parsed
