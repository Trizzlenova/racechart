from json import *
from .models import *
import json


with open('racechart/json/drivers.json') as driver_file:
    driver_data = json.loads(driver_file.read())

with open('racechart/json/race.json') as race_file:
    race_data = json.loads(race_file.read())
    # print(race_data['name'])

with open('racechart/json/standings.json') as standings_file:
    standings_data = json.loads(standings_file.read())
    # print(standings_data['drivers'][0]['full_name'])


print(driver_data['drivers'][0]['full_name'])

def cle


# def seed_driver(driver_dict):
#
#
# def seed_database(, , ):
#     for



#
# print(driver_data['drivers'][0])
#
# driver_json = open('racechart/json/drivers.json').read()
# driver_data = json.loads(driver_json, object_hook=Driver_File)
