from django.urls import path
from . import views

urlpatterns = [
  path('', views.see_css, name='see_css'),
  path('getall', views.get_all, name='get_all'),
  path('create_driver', views.create_driver, name='create_driver')
]
