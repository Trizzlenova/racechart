from django.db import models
from json import *
import json

class Team(models.Model):
  # from race
  name = models.CharField(max_length=1000, blank=True, null=True)
  crew_chief = models.CharField(max_length=1000, blank=True, null=True)
  manufacturer = models.CharField(max_length=1000, blank=True, null=True)
  sponsors = models.CharField(max_length=1000, blank=True, null=True)
  owner = models.CharField(max_length=2000, blank=True, null=True)

  def __str__(self):
    return self.name

  @classmethod
  def create(cls, team):
      new_team = cls(
        name = team['name'],
        # crew_chief = team['crew_chief'],
        manufacturer = team['manufacturer'],
        sponsors = team['sponsors'],
        owner = team['owner']
      )
      return new_team


class Driver(models.Model):
  team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='drivers', blank=True, null=True)
  # from driver
  full_name = models.CharField(max_length=100)
  birth_place = models.CharField(max_length=500)
  birthday = models.DateField()
  country = models.CharField(max_length=100)
  # dig down for this one
  car_number = models.IntegerField(blank=True, null=True)
  gender = models.CharField(max_length=1)
  height = models.IntegerField(blank=True, null=True)
  hobbies = models.CharField(max_length=500, blank=True, null=True)
  driver_id = models.CharField(max_length=100, blank=True, null=True)
  last_name = models.CharField(max_length=100)
  residence = models.CharField(max_length=200, blank=True, null=True)
  rookie_year = models.IntegerField(blank=True, null=True)
  status = models.CharField(max_length=100)
  twitter = models.CharField(max_length=100, blank=True, null=True)

# for loops will be dope

  def __str__(self):
    return self.full_name

  # driver['height'] = driver['height'] or 0

  @classmethod
  def create(cls, driver):
    new_driver = cls(
      team = driver['team'],
      full_name = driver['full_name'],
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
    # new_driver.save()
    return new_driver

  @classmethod
  def assign_team(cls, fk):
    cls['team'] = fk
    print(f'assigned a team to {cls.full_name}')

  class Meta:
    ordering = ['last_name']

class Standing(models.Model):
  driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='standings')
  # from standings
<<<<<<< HEAD
  avg_finish_position = models.IntegerField()
  avg_laps_completed = models.IntegerField()
  avg_start_postion = models.IntegerField()
=======
  avg_finish_position = models.FloatField()
  avg_laps_completed = models.FloatField()
  avg_start_postion = models.FloatField()
>>>>>>> 6b05b13956dc37b479ff9f7cc8c28aa668face27
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
      return self.driver.full_name

  class Meta:
    ordering = ['rank']

  @classmethod
  def create(cls, standing):

      new_standing = cls(
        driver = standing['driver'],
        avg_finish_position = standing['avg_finish_position'],
        avg_laps_completed = standing['avg_laps_completed'],
        avg_start_postion = standing['avg_start_position'],
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
      return new_standing


class Race(models.Model):
  # from race
  name = models.CharField(max_length=250)
  drivers = models.ManyToManyField(Driver, related_name='races')
  actual_distance = models.IntegerField(blank=True, null=True)
  avg_speed = models.DecimalField(max_digits=6, decimal_places=3)
  caution_laps = models.IntegerField(blank=True, null=True)
  cautions = models.CharField(max_length=250, blank=True, null=True)
  condition = models.CharField(max_length=250, blank=True, null=True)
  distance = models.IntegerField(blank=True, null=True)
  elapsed_time = models.CharField(max_length=250, blank=True, null=True)
  # count list length
  flags = models.IntegerField(blank=True, null=True)
  laps = models.IntegerField(blank=True, null=True)
  laps_completed = models.IntegerField(blank=True, null=True)
  lead_changes = models.IntegerField(blank=True, null=True)
  race_number = models.IntegerField(blank=True, null=True)
  scheduled_time = models.DateTimeField(blank=True, null=True)
  start_time = models.DateTimeField(blank=True, null=True)
  end_time = models.DateTimeField(blank=True, null=True)
  # convert from string to decimal
  victory_margin = models.DecimalField(max_digits=6, decimal_places=3)

  def __str__(self):
    return self.name

  @classmethod
  def create(cls, race):
      new_race = cls(
        name = race['name'],
        drivers = race['drivers'],
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
        # race_number = race['number'],
        scheduled_time = race['scheduled'],
        start_time = race['start_time'],
        end_time = race['end_time'],
        victory_margin = race['victory_margin'],
      )
      return new_race

class Result(models.Model):
  race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name='results')
  driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='results')
<<<<<<< HEAD
  avg_position = models.IntegerField(blank=True, null=True)
  avg_speed = models.IntegerField(blank=True, null=True)
  best_lap = models.IntegerField(blank=True, null=True)
  best_lap_speed = models.IntegerField(blank=True, null=True)
  best_lap_time = models.IntegerField(blank=True, null=True)
  bonus_points = models.IntegerField(blank=True, null=True)
  driver_rating = models.IntegerField(blank=True, null=True)
  elapsed_time = models.IntegerField(blank=True, null=True)
  fastest_laps = models.IntegerField(blank=True, null=True)
  laps_completed = models.IntegerField(blank=True, null=True)
  laps_led = models.IntegerField(blank=True, null=True)
  passes_made = models.IntegerField(blank=True, null=True)
  passing_differential = models.IntegerField(blank=True, null=True)
  penalty_points = models.IntegerField(blank=True, null=True)
=======
  avg_position = models.FloatField()
  avg_speed = models.FloatField()
  best_lap = models.IntegerField()
  best_lap_speed = models.FloatField()
  best_lap_time = models.FloatField()
  bonus_points = models.IntegerField()
  driver_rating = models.FloatField()
  elapsed_time = models.FloatField()
  fastest_laps = models.IntegerField()
  laps_completed = models.IntegerField()
  laps_led = models.IntegerField()
  passes_made = models.IntegerField()
  passing_differential = models.IntegerField()
  penalty_points = models.IntegerField()
>>>>>>> 6b05b13956dc37b479ff9f7cc8c28aa668face27
  #return length of the pit stop list
  pit_stops = models.IntegerField(blank=True, null=True)
  points = models.IntegerField(blank=True, null=True)
  position = models.IntegerField(blank=True, null=True)
  quality_passes = models.IntegerField(blank=True, null=True)
  start_position = models.IntegerField(blank=True, null=True)
  status = models.CharField(max_length=250, blank=True, null=True)
  times_led = models.IntegerField(blank=True, null=True)
  times_passed = models.IntegerField(blank=True, null=True)

  def __str__(self):
    return self.driver.full_name

  @classmethod
  def create(cls, result):
      new_result = cls(
        driver = result['driver'],
        race = result['race'],
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
        pit_stops = result['pit_stops'],
        points = result['points'],
        position = result['position'],
        quality_passes = result['quality_passes'],
        start_position = result['start_position'],
        status = result['status'],
        times_led = result['times_led'],
        times_passed = result['times_passed'],
      )
      return new_result
      # new_result.save()
