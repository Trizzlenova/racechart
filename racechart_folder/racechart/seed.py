from json import *
from racechart.models import Driver, Result, Race, Team, Standing
import json


                                              # ########################## #
                                              #         LOAD JSON          #
                                              # ########################## #
race_json = open('racechart/json/race.json').read()
loaded_race = json.loads(race_json)

driver_json = open('racechart/json/drivers.json').read()
loaded_drivers = json.loads(driver_json)

standings_json = open('racechart/json/standings.json').read()
loaded_standings = json.loads(driver_json)

drivers_array = loaded_drivers['drivers']
team_array = []

                                              # ########################## #
                                              #         CLEAR DATABASE     #
                                              # ########################## #

# def clear_database():
#     Driver.objects.all().clear()


for driver in drivers_array:
  crew_chief = None
  manufacturer = None
  owner = None
  name = driver['team']['name']
  sponsor = None

  if len(driver['cars']) > 0:
    if driver['cars'][0]['crew_chief']:
      crew_chief = driver['cars'][0]['crew_chief']
    manufacturer = driver['cars'][0]['manufacturer']['name']
    owner = driver['cars'][0]['owner']['name']
    sponsor = driver['cars'][0]['sponsors']

  match_found = False
  for team in team_array:
    if team == name:
      match_found = True

    if match_found == False:
      team_array.append(name)

print(team_array)
#
#
#
#
#
# # print(drivers[0]['full_name'])
#
# # for driver in drivers:
#   # drive = Driver.create(driver)
#   # drive.save()
#   # print(drive)
#
#
# REMEMBER TO CHANGE DRIVER ID AND CARS
necessary_driver_keys = ['full_name','birth_place', 'birthday', 'country', 'gender', 'height', 'hobbies', 'last_name', 'residence', 'rookie_year', 'status', 'twitter',]
necessary_race_keys = []
necessary_standing_keys = []
#
#
#                                               # ########################## #
#                                               # SEED DATABASE WITH TEAMS #
#                                               # ########################## #
#
#                                               # ########################## #
#                                               # SEED DATABASE WITH RESULTS #
#                                               # ########################## #
#
#                                               # ########################## #
#                                               # SEED DATABASE WITH STANDINGS #
#                                               # ########################## #
#
#
#                                               # ########################## #
#                                               # SEED DATABASE WITH RACES #
#                                               # ########################## #
# new_race = Race.create(loaded_race)
# new_race.save()
# # print(loaded_race['name'])
#
#
                                              # ########################## #
                                              # SEED DATABASE WITH DRIVERS #
                                              # ########################## #
def seed_drivers():
  for single_driver in drivers_array:

    given_keys = list(single_driver.keys())
    single_driver['car_number'] = None
    keys_to_add = []

    for wanted_key in necessary_driver_keys:
      match_found = False
      for key in given_keys:
        if wanted_key == key:
          match_found = True
      if match_found == False:
        keys_to_add.append(wanted_key)



    for key in single_driver:

      if type(single_driver[key]) == list and len(single_driver[key]) > 0:

        car_number = single_driver[key][0]['number']
        single_driver['car_number'] = car_number

    if len(keys_to_add) > 0:
      for key in keys_to_add:
        single_driver[key] = None

    new_driver = Driver.create(single_driver)
    new_driver.save()





for driver in drivers:
  print(driver['full_name'])
