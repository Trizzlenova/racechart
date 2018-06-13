from django.db import models
from json import *

class Driver(models.Model):
  full_name = models.CharField(max_length=100)
  birth_place = models.CharField(max_length=500)
  birthday = models.DateField()
  country = models.CharField(max_length=100)
  # cars
  def __str__(self):
    return self.full_name

  @classmethod
  def create(cls, full_name, birth_place, birthday, country):
      driver = cls(full_name=full_name, birth_place=birth_place, birthday=birthday, country=country)
      # do something with the driver
      return driver


# tommy = Driver.create('Tommy Trucker', 'Mobile, Alabama', '1985-01-01', 'Murica')
# tommy.save()
# print(f'I am printing {tommy.full_name} from {tommy.country}')
# "UNITED STATES"
# first_name
# :
# "David"
# full_name
# :
# "David Ragan"
# gender
# :
# "M"
# height
# :
# 72
# hobbies
# :
# "Boxing, restoring old cars, hunting, fishing"
# id
# :
# "25884070-3ded-4fdc-9370-d09428ac95e4"
# last_name
# :
# "Ragan"
# points_eligible
# :
# true
# residence
# :
# "Huntersville, North Carolina, United States"
# rookie_year
# :
# 2007
# status
# :
# "ACT"
# team
# :
# {id: "bd38dfec-bb97-4f29-b032-cc6f0c77dfe6", name: "Front Row Motorsports"}
# twitter
# :
# "@DavidRagan"

#

# # for loops will be dope

# # sue = Driver.create('Sue Redneck')
# # sue.save()
# # print(f'I am printing {sue.name}')
