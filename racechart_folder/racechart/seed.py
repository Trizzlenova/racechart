from json import *
from racechart.models import Driver, Result, Race, Team, Standing
import json



# with open('racechart/json/drivers.json') as driver_file:
#     driver_data = json.loads(driver_file.read())

# with open('racechart/json/race.json') as race_file:
#     race_data = json.loads(race_file.read())
#     # print(race_data['name'])

# with open('racechart/json/standings.json') as standings_file:
#     standings_data = json.loads(standings_file.read())
    # print(standings_data['drivers'][0]['full_name'])

driver_json = open('racechart/json/drivers.json').read()
loaded = json.loads(driver_json)

drivers_array = loaded['drivers']

# print(drivers[0]['full_name'])

# for driver in drivers:
  # drive = Driver.create(driver)
  # drive.save()
  # print(drive)


# REMEMBER TO CHANGE DRIVER ID AND CARS
necessary_driver_keys = ['full_name',
                'birth_place',
                'birthday',
                'country',
                'gender',
                'height',
                'hobbies',
                'last_name',
                'residence',
                'rookie_year',
                'status',
                'twitter',
              ]






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





# for driver in drivers:
#   print(driver['full_name'])
