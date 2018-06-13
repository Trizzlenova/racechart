from django.shortcuts import render
from requests import *
import json
from django.http import HttpResponse, HttpResponseRedirect

drivers = []

def home(requests):
  # hide key before pushing to git
  # url =''
  response = get(url)
  parsed = json.loads(response.content)
  drivers = parsed
  return HttpResponseRedirect('/')

