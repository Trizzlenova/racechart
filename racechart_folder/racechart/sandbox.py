def clear_database():
    Driver.objects.all().delete()
    Team.objects.all().delete()
    Race.objects.all().delete()
    Result.objects.all().delete()
    Standing.objects.all().delete()
    print('cleared the database')


def seed_teams():
    driver_json = open('racechart/json/drivers.json').read()
    loaded_drivers = json.loads(driver_json)
    driver_list = loaded_drivers['drivers']
    for individual_driver in driver_list:

## Make a Team dictionary with default values
      team = {
        'crew_chief': None,
        'manufacturer': None,
        'owner': None,
        'name': individual_driver['team']['name'],
        'sponsors': None,
      }

## Find the list of cars, replace default values

      cars = individual_driver['cars']
      if len(cars) > 0:
          team['manufacturer'] = cars[0]['manufacturer']['name']
          team['owner'] = individual_driver['cars'][0]['owner']['name']
          team['sponsors'] = individual_driver['cars'][0]['sponsors']
          for key in cars[0]:
              if key == ['crew_chief']:
                  team['crew_chief'] = cars[0]['crew_chief']

      team_array.append(team)

# Check to make sure we don't make identical teams

    for added_team in team_array:
      match_found = False

      for cleaned_team in cleaned_teams:

        if added_team['name'] == cleaned_team['name']:
          match_found = True

      if match_found == False:
        cleaned_teams.append(added_team)

    for team in cleaned_teams:
      new_team = Team.create(team)
      new_team.save()
      print(new_team)


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


def seed_races():
    race_json = open('racechart/json/race.json').read()
    loaded_race = json.loads(race_json)
    new_race = Race.create(loaded_race)
    new_race.save()
    print(new_race)

def seed_results():
    race_json = open('racechart/json/race.json').read()
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

def seed_standings():
    standings_json = open('racechart/json/standings.json').read()
    loaded_standings = json.loads(standings_json)
    driver_standings = loaded_standings['drivers']

    for standing in driver_standings:
        standing['driver'] = Driver.objects.get(full_name=standing['full_name'])

        for key in standing:
            if type(standing[key]) == float:
                standing[key] = round(standing[key], 2)

        new_standing = Standing.create(standing)
        new_standing.save()
        print(new_standing)

def seed_database():
    clear_database()
    seed_teams()
    seed_drivers()
    seed_races()
    seed_results()
    seed_standings()
    print('seeded database')
