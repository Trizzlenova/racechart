from django.db import models
from json import *

class Driver(models.Model):
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

class Team(models.Model):
  name = models.CharField(max_length=100)
  crew_chief = models.CharField(max_length=100)
  manufacturer = models.CharField(max_length=100)
  sponsors = models.CharField(max_length=200)

  def __str__(self):
    return self.name

  # add classmethod

class Race(models.Model):
  name = models.CharField(max_length=250)
  actual_distance = models.IntegerField()
  avg_speed = models.DecimalField(max_digits=5, decimal_places=3)
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
  victory_margin = models.DecimalField(max_digits=5, decimal_places=3)


