def seed_races():
    cleaned_races = []
    i = 0
    while i < 10:
        race_json = open(f'racechart/json/race_list/race{i}.json').read()
        loaded_race = json.loads(race_json)
        race_name = loaded_race['name']
        loaded_race['race_number'] = None

        loaded_race['actual_distance'] = float(loaded_race['avg_speed'])
        loaded_race['victory_margin'] = float(loaded_race['victory_margin'])

        wanted_keys = ['name','drivers','actual_distance','avg_speed','caution_laps','cautions','condition','distance','elapsed_time','laps','laps_completed','lead_changes','scheduled_time','start_time','end_time','victory_margin', 'number', 'flags']

        for key in loaded_race:
            if key == 'flags':
                loaded_race['flags'] = len(loaded_race['flags'])
            if key == 'number':
                loaded_race['race_number'] = int(loaded_race['number'])

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
        # print(loaded_race)
        cleaned_races.append(loaded_race)

        i = i + 1

    for cleaned_race in cleaned_races:
        new_race = Race.create(cleaned_race)
        new_race.save()
        print(new_race)
        print('wow')

def seed_results():
    cleaned_results = []
    i = 0
    while i < 10:
      race_json = open(f'racechart/json/race_list/race{i}.json').read()
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
