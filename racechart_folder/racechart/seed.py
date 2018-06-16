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
                        #     CLEAR THE DATABASE     #
                        # ########################## #

Driver.objects.all().delete()
Team.objects.all().delete()
Race.objects.all().delete()
Result.objects.all().delete()
Standing.objects.all().delete()
print('cleared the database')


drivers_array = loaded_drivers['drivers']
necessary_race_keys = []
necessary_standing_keys = []
                        # ########################## #
                        #       CLEAN THE DATA       #
                        # ########################## #


cleaned_teams = []
team_array = []


############## TEAMS ###################

  # iterate through each driver
for individual_driver in drivers_array:

  team = {
    # 'crew_chief': None,
    'manufacturer': None,
    'owner': None,
    'name': individual_driver['team']['name'],
    'sponsors': None,
  }

  for key in individual_driver:

    # find the array of cars, and
    if type(individual_driver[key]) == list and len(individual_driver[key]) > 0:
      # team['crew_chief'] = individual_driver['cars'][0]['crew_chief']
      team['manufacturer'] = individual_driver['cars'][0]['manufacturer']['name']
      team['owner'] = individual_driver['cars'][0]['owner']['name']
      team['sponsors'] = individual_driver['cars'][0]['sponsors']

  team_array.append(team)
# print(len(team_array))

# Check to make sure we don't make identical teams

for added_team in team_array:
  match_found = False

  for cleaned_team in cleaned_teams:

    if added_team['name'] == cleaned_team['name']:
      match_found = True

  if match_found == False:
      # print(team)
    cleaned_teams.append(added_team)


for team in cleaned_teams:
  new_team = Team.create(team)
  new_team.save()
  # print(new_team)

# ############## DRIVERS ###################



cleaned_drivers = []

# iterate through each driver
for single_driver in drivers_array:

  # declare values in case any drivers are missing
  single_driver['car_number'] = None

  # array of values required for model
  necessary_driver_keys = ['full_name','birth_place', 'birthday', 'country', 'gender', 'height', 'hobbies', 'last_name', 'residence', 'rookie_year', 'status', 'twitter',]

#### assign teams

  team_name = single_driver['team']['name']
  associated_team = Team.objects.get(name=team_name)

  single_driver['team'] = associated_team

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

for cleaned_driver in cleaned_drivers:

  new_driver = Driver.create(cleaned_driver)
  new_driver.save()
  # print(new_driver)

                ######################
                ######## RACES #######
                ######################

results = loaded_race['results']
race_drivers = []

new_race = Race.create(loaded_race)
new_race.save()

                ######################
                ####### RESULTS ######
                ######################

for result in results:
    driver_binary = len(Driver.objects.filter(full_name=result['driver']['full_name']))
    print('Result')
    print(result['driver']['full_name'])
    print('')

    if driver_binary == 1:
        result['driver'] = Driver.objects.get(full_name=result['driver']['full_name'])
        print(result['driver'])
        result['race'] = new_race
        result['pit_stops'] = len(result['pit_stops'])

        for key in result:
            if type(result[key]) == float:
                result[key] = round(result[key], 0)
                result[key] = int(result[key])
                print(f'{key}: {type(result[key])}')


        new_result = Result.create(result)
        new_result.save()
        print(new_result)

print(loaded_race['name'])
#
# print('seeded teams, drivers and races')
