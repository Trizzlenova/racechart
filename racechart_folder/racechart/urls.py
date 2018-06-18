from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
  path('', views.standing_list, name="standing_list"),
  path('getall', views.get_all_races, name='get_all_races'),
  path('drivers/', views.driver_list, name='driver_list'),
  path('drivers/<int:pk>', views.driver_detail, name='driver_detail'),
  path('standings/', views.standing_list, name='standing_list'),
  # path('results/', views.result_detail, name='result_detail'),
]
