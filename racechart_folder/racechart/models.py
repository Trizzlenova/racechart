from django.db import models
from json import *

class Driver_File:
  def __init__(self, data):
    self.__dict__ = data

driver_json = open('racechart/json/drivers.json').read()
driver_data = json.loads(driver_json, object_hook=Driver_File)


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
  def create(cls):
    driver_json = open('racechart/json/drivers.json').read()
    from_string_to_json = json.loads(driver_json)
    drivers = from_string_to_json['drivers']
    for driver_instance in drivers:
      driver = cls(
        birth_place = driver_instance['birth_place'],
        birthday = driver_instance['birthday'],
        country = driver_instance['country'],
        car_number = driver_instance['car_number'],
        gender = driver_instance['gender'],
        height = driver_instance['height'],
        hobbies = driver_instance['hobbies'],
        driver_id = driver_instance['id'],
        last_name = driver_instance['last_name'],
        residence = driver_instance['residence'],
        rookie_year = driver_instance['rookie_year'],
        status = driver_instance['status'],
        twitter = driver_instance['twitter'],
        )
      driver.save()

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
