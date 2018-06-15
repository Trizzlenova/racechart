from json import *
from racechart.models import Driver, Result, Race, Team, Standing
import json

                        # ########################## #
                        #       LOAD JSON FILES      #
                        # ########################## #

race_json = open('racechart/json/race.json').read()
loaded_race = json.loads(race_json)

driver_json = open('racechart/json/drivers.json').read()
loaded_drivers = json.loads(driver_json)

standings_json = open('racechart/json/standings.json').read()
loaded_standings = json.loads(driver_json)

                        # ########################## #
                        #     HELPER FUNCTIONS       #
                        # ########################## #

def clear_database():
  Driver.objects.all().delete()
  Team.objects.all().delete()
  Race.objects.all().delete()
  Result.objects.all().delete()
  Standing.objects.all().delete()



drivers_array = loaded_drivers['drivers']
necessary_race_keys = []
necessary_standing_keys = []
                        # ########################## #
                        #       CLEANER FUNCTIONS       #
                        # ########################## #
def clean_team_data():
  # output array
  cleaned_teams = []
  team_array = []


  # iterate through each driver
  for single_driver in drivers_array:

    team = {
      # 'crew_chief': None,
      'manufacturer': None,
      'owner': None,
      'name': single_driver['team']['name'],
      'sponsor': None,
    }
    for key in single_driver:

      # find the array of cars, and
      if type(single_driver[key]) == list and len(single_driver[key]) > 0:
        # team['crew_chief'] = single_driver['cars'][0]['crew_chief']
        team['manufacturer'] = single_driver['cars'][0]['manufacturer']['name']
        team['owner'] = single_driver['cars'][0]['owner']['name']
        team['sponsor'] = single_driver['cars'][0]['sponsors']

# Check to make sure we don't make identical teams
    match_found = False
    for added_team in team_array:
      if added_team == team['name']:
        match_found = True

      if match_found == False:
        team_array.append(name)
        cleaned_teams.append(team)

  return cleaned_teams


def clean_driver_data():

  # output array

  cleaned_drivers = []

  # iterate through each driver
  for single_driver in drivers_array:

    # declare values in case any drivers are missing
    single_driver['car_number'] = None

    # array of values required for model
    necessary_driver_keys = ['full_name','birth_place', 'birthday', 'country', 'gender', 'height', 'hobbies', 'last_name', 'residence', 'rookie_year', 'status', 'twitter',]


    # keys provided by API
    provided_keys = list(single_driver.keys())
    keys_to_add = []

    # Check if the drivers contain the keys needed
    for wanted_key in necessary_driver_keys:

      match_found = False

      for key in provided_keys:
        if wanted_key == key:
          match_found = True
        # if no match is found, add key name to array
      if match_found == False:
        keys_to_add.append(wanted_key)

# Add missing keys to driver.
# Also, make car_number match the number of first car in driver's array of cars

    for key in single_driver:

      # find the array of cars, and
      if type(single_driver[key]) == list and len(single_driver[key]) > 0:

        car_number = single_driver[key][0]['number']
        single_driver['car_number'] = car_number

    if len(keys_to_add) > 0:
      for key in keys_to_add:
        single_driver[key] = None

    cleaned_drivers.append(single_driver)

  return cleaned_drivers








def seed_drivers():
  driver_list = clean_driver_data()
  for driver in driver_list:
    new_driver = Driver.create(driver)
    new_driver.save()

def seed_teams():
  team_list = clean_team_data()
  for team in team_list:
    new_team = Team.create(team)
    new_team.save()
    print(new_team)


def seed_database():
  seed_teams(team_list)
  seed_drivers(driver_list)

  print('seeded teams and drivers')

# clear_database()
# seed_database()

seed_teams()
