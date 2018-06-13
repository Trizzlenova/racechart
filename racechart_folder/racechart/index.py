from requests import *
import json
from models import Driver
# from django.http import HttpResponse, HttpResponseRedirect

drivers = []


if drivers == []:
  # url = ''
  response = get(url)
  parsed = json.loads(response.content)
  drivers = parsed
  # return HttpResponseRedirect('/')
  print('called drivers')

new_driver = Driver.create(drivers['drivers'][0]['full_name'])
print(new_driver)
