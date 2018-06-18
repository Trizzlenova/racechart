
from itertools import count
# from sleepy import buzzergen


# print('Hello, World!')

def add(a, b):
  return a + b

def subt(a, b):
  return a - b

def mult(a, b):
  return a * b

import time

while True:
  # function here
  time.sleep(5)
  # function here
  time.sleep(5)
  # function here
  break

# class Async:
#   def __init__(self, func, args):
#     self.func = func
#     self.args = args

#   def inlined_async(func):
#     @wraps(func)
#     def wrapper(*args):
#       f = func(*args)
#       result_queue = Queue()
#       result_queue.put(None)
#       while True:
#         result = result_queue.get()
#         try:
#           a = f.send(result)
#           apply_async(a.func, a.args, callback=result_queue.put)
#         except StopIteration:
#           break
#     return wrapper

#   def add(x, y):
#     return x + y

#   @inlined_async
#   def test():
#     r = yield Async(add, (2,3))
#     print(r)
#     r = yield Async(add, ('hello', 'world'))
#     print(r)
#     for n in range(10):
#       r = yield Async(add, (n, n))
#       print(r)
#     print('Goodbye')


# Playing around with workers


# def worker():
#     while True:
#         item = q.get()
#         if item is None:
#             break
#         do_work(item)
#         q.task_done()


def seed_drivers():
    cleaned_drivers = []
    driver_json = open('racechart/json/drivers.json').read()
    loaded_drivers = json.loads(driver_json)
    driver_list = loaded_drivers['drivers']
    # iterate through each driver
    for driver in driver_list:
      # default value for drivers missing car data
      driver['car_number'] = None
      # array of values required for model
      wanted_keys = ['full_name','birth_place', 'birthday', 'country', 'gender', 'height', 'hobbies', 'last_name', 'residence', 'rookie_year', 'status', 'twitter',]
    #### assign teams
      team_name = driver['team']['name']
      associated_team = Team.objects.get(name=team_name)
      driver['team'] = associated_team
      # keys provided by API
      provided_keys = list(driver.keys())
      keys_to_add = []

      # Check if the drivers contain the keys needed
      for wanted_key in wanted_keys:
        match_found = False
        for key in provided_keys:
          if wanted_key == key:
            match_found = True
          # if no match is found, add key name to array
        if match_found == False:
          keys_to_add.append(wanted_key)

    # Add missing keys to driver.
    # Also, make car_number match the number of first car in driver's array of cars
      if len(driver['cars']) > 0:
          driver['car_number'] = driver['cars'][0]['number']
    # Set missing keys to None
      if len(keys_to_add) > 0:
        for key in keys_to_add:
          driver[key] = None
      cleaned_drivers.append(driver)

    for cleaned_driver in cleaned_drivers:
      new_driver = Driver.create(cleaned_driver)
      new_driver.save()
      print(new_driver)

import json
def seed_races():
cleaned_races = []
# i = 0
# while i < 5:
race_json = open(f'racechart/json/race_list/race1.json').read()
loaded_race = json.loads(race_json)
race_name = loaded_race['name']
print(race_name)
wanted_keys = ['name','drivers','actual_distance','avg_speed','caution_laps','cautions','condition','distance','elapsed_time','flags','laps','laps_completed','lead_changes','scheduled_time','start_time','end_time','victory_margin',]
# associated_race = Race.objects.get(name=race_name)
provided_keys = list(loaded_race.keys())
keys_to_add = []

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
cleaned_races.append()

for cleaned_race in cleaned_races:
    new_race = Race.create(cleaned_race)
    new_race.save()
    print(new_race)

    # i = i + 1

                ######################
                ####### RESULTS ######
                ######################

def seed_results():
    cleaned_results = []
    i = 0
    while i < 5:
      race_json = open(f'racechart/json/race{i}.json').read()
      loaded_race = json.loads(race_json)
      results = loaded_race['results']

      for result in results:
  # Switch triggers if driver exists in database. This is to avoid No Matching Query error
          driver_binary = len(Driver.objects.filter(full_name=result['driver']['full_name']))
          if driver_binary == 1:
              result['driver'] = Driver.objects.get(full_name=result['driver']['full_name'])
              result['race'] = Race.objects.all()[0]
              result['pit_stops'] = len(result['pit_stops'])

  ## Round the floats to 2 decimal places
              for key in result:
                  if type(result[key]) == float:
                      result[key] = round(result[key], 2)

              new_result = Result.create(result)
              new_result.save()
              print(new_result)
      i = i + 1
