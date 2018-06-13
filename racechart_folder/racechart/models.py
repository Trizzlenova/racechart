from django.db import models
# from .api_calls import drivers

class Driver(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

  @classmethod
  def create(cls, name):
      driver = cls(name=name)
      # do something with the driver
      return driver

sue = Driver.create('Sue Redneck')
sue.save()
print(f'I am printing {sue.name}')
