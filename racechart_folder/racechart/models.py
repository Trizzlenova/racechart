from django.db import models
from json import *


class Driver(models.Model):
  # team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='drivers')
  # from driver
  full_name = models.CharField(max_length=100)
  birth_place = models.CharField(max_length=500)
  birthday = models.DateField()
  country = models.CharField(max_length=100)
  # dig down for this one
  car_number = models.IntegerField()
  gender = models.CharField(max_length=1)
  height = models.IntegerField()
  hobbies = models.CharField(max_length=500, blank=True, null=True)
  driver_id = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  residence = models.CharField(max_length=200)
  rookie_year = models.IntegerField()
  status = models.CharField(max_length=100)
  twitter = models.CharField(max_length=100)

# for loops will be dope

  def __str__(self):
    return self.full_name

  @classmethod
  def create(cls, driver):
    # driver_json = open('racechart/json/drivers.json').read()
    # from_string_to_json = json.loads(driver_json)
    # drivers = from_string_to_json['drivers']
    # for driver_instance in drivers:
      new_driver = cls(
        birth_place = driver['birth_place'],
        birthday = driver['birthday'],
        country = driver['country'],
        car_number = driver['car_number'],
        gender = driver['gender'],
        height = driver['height'],
        hobbies = driver['hobbies'],
        driver_id = driver['id'],
        last_name = driver['last_name'],
        residence = driver['residence'],
        rookie_year = driver['rookie_year'],
        status = driver['status'],
        twitter = driver['twitter'],
        )
      # driver.save()

  class Meta:
    ordering = ['last_name']

class Standing(models.Model):
  driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='standings')
  # from standings
  avg_finish_position = models.DecimalField(max_digits=6, decimal_places=3)
  avg_laps_completed = models.DecimalField(max_digits=6, decimal_places=3)
  avg_start_postion = models.DecimalField(max_digits=6, decimal_places=3)
  chase_bonus = models.IntegerField()
  dnf = models.IntegerField()
  full_name = models.CharField(max_length=200)
  in_chase = models.BooleanField()
  laps_completed = models.IntegerField()
  laps_led = models.IntegerField()
  laps_led_pct = models.IntegerField()
  points = models.IntegerField()
  poles = models.IntegerField()
  rank = models.IntegerField()
  stage_wins = models.IntegerField()
  starts = models.IntegerField()
  status = models.CharField(max_length=200)
  top_5 = models.IntegerField()
  top_10 = models.IntegerField()
  top_15 = models.IntegerField()
  top_20 = models.IntegerField()
  wins = models.IntegerField()

  def __str__(self):
      return (f`{self.full_name} standing`)

  @classmethod
  def create(cls, standing):

      new_standing = cls(
        avg_finish_position = standing['avg_finish_position'],
        avg_laps_completed = standing['avg_laps_completed'],
        avg_start_postion = standing['avg_start_postion'],
        chase_bonus = standing['chase_bonus'],
        dnf = standing['dnf'],
        full_name = standing['full_name'],
        in_chase = standing['in_chase'],
        laps_completed = standing['laps_completed'],
        laps_led = standing['laps_led'],
        laps_led_pct = standing['laps_led_pct'],
        points = standing['points'],
        poles = standing['poles'],
        rank = standing['rank'],
        stage_wins = standing['stage_wins'],
        starts = standing['starts'],
        status = standing['status'],
        top_5 = standing['top_5'],
        top_10 = standing['top_10'],
        top_15 = standing['top_15'],
        top_20 = standing['top_20'],
        wins = standing['wins'],
      )

  class Meta:
    ordering = ['rank']

class Team(models.Model):
  # from race
  name = models.CharField(max_length=100)
  crew_chief = models.CharField(max_length=100)
  manufacturer = models.CharField(max_length=100)
  sponsors = models.CharField(max_length=200)

  def __str__(self):
    return self.name

  @classmethod
  def create(cls, team):
      new_team = cls(
        name = team['name'],
        crew_chief = team['crew_chief'],
        manufacturer = team['manufacturer'],
        sponsors = team['sponsors'],
      )

  # add classmethod

class Race(models.Model):
  # from race
  name = models.CharField(max_length=250)
  drivers = models.ManyToManyField(Driver, related_name='races')
  actual_distance = models.IntegerField()
  avg_speed = models.DecimalField(max_digits=6, decimal_places=3)
  caution_laps = models.IntegerField()
  cautions = models.CharField(max_length=250)
  condition = models.CharField(max_length=250)
  distance = models.IntegerField()
  elapsed_time = models.CharField(max_length=250)
  # count list length
  flags = models.IntegerField()
  laps = models.IntegerField()
  laps_completed = models.IntegerField()
  lead_changes = models.IntegerField()
  race_number = models.IntegerField()
  scheduled_time = models.DateTimeField()
  start_time = models.DateTimeField()
  end_time = models.DateTimeField()
  # convert from string to decimal
  victory_margin = models.DecimalField(max_digits=6, decimal_places=3)

  def __str__(self):
    return self.name

  @classmethod
  def create(cls, race):
      new_race = cls(
        actual_distance = race['actual_distance'],
        avg_speed = race['avg_speed'],
        caution_laps = race['caution_laps'],
        cautions = race['cautions'],
        condition = race['condition'],
        distance = race['distance'],
        elapsed_time = race['elapsed_time'],
        flags = len(race['flags']),
        laps = race['laps'],
        laps_completed = race['laps_completed'],
        lead_changes = race['lead_changes'],
        race_number = race['race_number'],
        scheduled_time = race['scheduled_time'],
        start_time = race['start_time'],
        end_time = race['end_time'],
        victory_margin = race['victory_margin'],
      )

class Result(models.Model):
  race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name='results')
  driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='results')
  avg_position = models.DecimalField(max_digits=6, decimal_places=3)
  avg_speed = models.DecimalField(max_digits=6, decimal_places=3)
  best_lap = models.IntegerField()
  best_lap_speed = models.DecimalField(max_digits=6, decimal_places=3)
  best_lap_time = models.DecimalField(max_digits=6, decimal_places=3)
  bonus_points = models.IntegerField()
  driver_rating = models.DecimalField(max_digits=6, decimal_places=3)
  elapsed_time = models.DecimalField(max_digits=6, decimal_places=3)
  fastest_laps = models.IntegerField()
  laps_completed = models.IntegerField()
  laps_led = models.IntegerField()
  passes_made = models.IntegerField()
  passing_differential = models.IntegerField()
  penalty_points = models.IntegerField()
  #return length of the pit stop list
  pit_stops = models.IntegerField()
  points = models.IntegerField()
  position = models.IntegerField()
  quality_passes = models.IntegerField()
  start_position = models.IntegerField()
  status = models.CharField(max_length=250)
  times_led = models.IntegerField()
  times_passed = models.IntegerField()

  def __str__(self):
    return self.race.name

  @classmethod
  def create(cls, result):
      new_result = cls(
        avg_position = result['avg_position'],
        avg_speed = result['avg_speed'],
        best_lap = result['best_lap'],
        best_lap_speed = result['best_lap_speed'],
        best_lap_time = result['best_lap_time'],
        bonus_points = result['bonus_points'],
        driver_rating = result['driver_rating'],
        elapsed_time = result['elapsed_time'],
        fastest_laps = result['fastest_laps'],
        laps_completed = result['laps_completed'],
        laps_led = result['laps_led'],
        passes_made = result['passes_made'],
        passing_differential = result['passing_differential'],
        penalty_points = result['penalty_points'],
        pit_stops = len(result['pit_stops']),
        points = result['points'],
        position = result['position'],
        quality_passes = result['quality_passes'],
        start_position = result['start_position'],
        status = result['status'],
        times_led = result['times_led'],
        times_passed = result['times_passed'],
      )
