from django.shortcuts import render
from requests import *
from .models import Driver, Result, Race, Team, Standing
import json
from json import *
from django.http import HttpResponse, HttpResponseRedirect
# from racechart_folder.config import API_KEY
from rest_framework import generics
from .serializers import *
import os
# from .tasks import access_nascar_api


api = os.profile['API_KEY']
year = '2018'

race_list_url = f'http://api.sportradar.us/nascar-t3/mc/{year}/races/schedule.json?api_key={api}'
race_list_file = 'racechart/json/race_list.json'

race_ids = []

race_json = open('racechart/json/race_list.json').read()
loaded = json.loads(race_json)
event_list = loaded['events']
for events in event_list:
  races = events['races']
  for race in races:
    race_ids.append(race['id'])

driver_url = f'http://api.sportradar.us/nascar-ot3/mc/{year}/drivers/list.json?api_key={api}'
driver_file = 'racechart/json/drivers.json'

# race_url = f'http://api.sportradar.us/nascar-ot3/mc/races/{race_ids}/results.json?api_key={api}'
race_file = 'racechart/json/race.json'

standings_url = f'http://api.sportradar.us/nascar-ot3/mc/{year}/standings/drivers.json?api_key={api}'
standings_file = 'racechart/json/standings.json'

# def see_css(request):
#     return render(request, 'racechart/driver_list.html')

def grab_json(request, url, data_file):
  response = get(url)
  content = response.content
  data = open(data_file, 'wb')
  data.write(content)
  data.close()
  print(f'you are grabbing a json from {url}')

def get_all(request):
  # grab_json(request, driver_url, driver_file)
  # grab_json(request, race_url, race_file)
  # grab_json(request, standings_url, standings_file)
  # grab_json(request, race_list_url, race_list_file)
  return HttpResponseRedirect('/admin')

race_folder = 'racechart/json/race_list/race.json'

import time
def get_all_races(request):
  i = 0
  length = len(race_ids)
  while(i < 10):
    race_url = f'http://api.sportradar.us/nascar-ot3/mc/races/{race_ids[i]}/results.json?api_key={api}'
    grab_json(request, race_url, f'racechart/json/race_list/race{i}.json')
    print(f'you are grabbing a json from {race_url}')
    time.sleep(3)
    if i > 8:
      print('Grabbed all races!')
      # return HttpResponseRedirect('/admin')
    i = i + 1

def driver_list(request):
    drivers = Driver.objects.all()
    return render(request, 'racechart/driver_list.html', {'drivers': drivers})

def driver_detail(request, pk):
    driver = Driver.objects.get(id=pk)
    return render(request, 'racechart/driver_detail.html', {'driver': driver})

def team_list(request):
    teams = Team.objects.all()
    return render(request, 'racechart/team_list.html', {'teams': teams})

def team_detail(request, pk):
    team = Team.objects.get(id=pk)
    return render(request, 'racechart/team_detail.html', {'team': team})

def race_list(request):
    races = Race.objects.all()
    return render(request, 'racechart/race_list.html', {'races': races})

def race_detail(request, pk):
    race = Race.objects.get(id=pk)
    return render(request, 'racechart/race_detail.html', {'race': race})

def standing_list(request):
    standings = Standing.objects.all()
    return render(request, 'racechart/standing_list.html', {'standings': standings})

def standing_detail(request, pk):
    standings = Standing.objects.get(id=pk)
    return render(request, 'racechart/standing_list.html', {'standing': standing})

def result_list(request):
    results = Result.objects.all()
    return render(request, 'racechart/result_list.html', {'results': results})

def result_detail(request, pk):
    result = Result.objects.get(id=pk)
    return render(request, 'racechart/result_detail.html', {'result': result})

class RaceList(generics.ListCreateAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer

class RaceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer

class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class StandingList(generics.ListCreateAPIView):
    queryset = Standing.objects.all()
    serializer_class = StandingSerializer

class StandingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Standing.objects.all()
    serializer_class = StandingSerializer

class ResultList(generics.ListCreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

class ResultDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

class DriverList(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class DriverDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
