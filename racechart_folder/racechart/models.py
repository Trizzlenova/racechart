from django.db import models
from json import *

class Driver(models.Model):
  # from driver
  full_name = models.CharField(max_length=100)
  birth_place = models.CharField(max_length=500)
  birthday = models.DateField()
  country = models.CharField(max_length=100)
  car_number = models.IntegerField()
  gender = models.CharField(max_length=1)
  height = models.IntegerField()
  hobbies = models.CharField(max_length=500, blank=True, null=True)
  driver_id = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  residence = models.CharField(max_length=200)
  rookie_year = models.IntegerField()
  status = models.CharField(max_length=100)
  team = models.ForeignKey(Team, on_delete=CASCADE, related_name='drivers')
  twitter = models.CharField(max_length=100)

# for loops will be dope

  def __str__(self):
    return self.full_name

  @classmethod
  def create(cls, full_name, birth_place, birthday, country):
      driver = cls(full_name=full_name, birth_place=birth_place, birthday=birthday, country=country)
      # do something with the driver
      return driver

class Standing(models.Model):
  driver = models.ForeignKey(Driver, on_delete=CASCADE, related_name='standings')
  # from standings
  avg_finish_position = models.DecimalField(max_digits=None, decimal_places=None)
  avg_laps_completed = models.DecimalField(max_digits=None, decimal_places=None)
  avg_start_postion = models.DecimalField(max_digits=None, decimal_places=None)
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
  avg_speed = models.DecimalField(max_digits=None, decimal_places=None)
  caution_laps = models.IntegerField()
  cautions = models.CharField(max_length=250)
  condition = models.CharField(max_length=250)
  distance = models.IntegerField()
  elapsed_time = models.CharField(max_length=250)
  laps = models.IntegerField()
  laps_completed = models.IntegerField()
  lead_changes = models.IntegerField()
  race_number = models.IntegerField()
  scheduled_time = models.DateTimeField()
  start_time = models.DateTimeField()
  end_time = models.DateTimeField()
  # convert from string to decimal
  victory_margin = models.DecimalField(max_digits=None, decimal_places=None)

  def __str__(self):
    return self.name

class Result(models.Model):
  race = models.ForeignKey(Race, on_delete=CASCADE, related_name='results')
  driver = models.ForeignKey(Driver, on_delete=CASCADE, related_name='results')
  avg_position = models.DecimalField(max_digits=None, decimal_places=None)
  avg_speed = models.DecimalField(max_digits=None, decimal_places=None)
  best_lap = models.IntegerField()
  best_lap_speed = models.DecimalField(max_digits=None, decimal_places=None)
  best_lap_time = models.DecimalField(max_digits=None, decimal_places=None)
  bonus_points = models.IntegerField()
  driver_rating = models.DecimalField(max_digits=None, decimal_places=None)
  elapsed_time = models.DecimalField(max_digits=None, decimal_places=None)
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
