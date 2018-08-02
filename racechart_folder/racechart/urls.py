from django.urls import path, include
from django.conf.urls import url
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
  path('', views.standing_list, name="standing_list"),
  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
  url(r'api/races/$', views.RaceList.as_view()),
  path('api/races/<int:pk>', views.race_detail, name="race_detail"),
  url(r'api/drivers/$', views.DriverList.as_view()),
  url(r'api/drivers/(?P<pk>[0-9]+)/$', views.DriverDetail.as_view()),
  url(r'api/teams/$', views.TeamList.as_view()),
  path('api/teams/<int:pk>', views.team_detail, name="team_detail"),
  url(r'api/standings/$', views.StandingList.as_view()),
  url(r'api/standings/(?P<pk>[0-9]+)/$', views.StandingList.as_view()),
  url(r'api/results/$', views.ResultList.as_view()),
  url(r'api/results/(?P<pk>[0-9]+)/$', views.ResultDetail.as_view()),
  path('getall', views.csv_boi, name='csv_boi'),
  path('drivers/', views.driver_list, name='driver_list'),
  path('drivers/<int:pk>', views.driver_detail, name='driver_detail'),
  path('standings/', views.standing_list, name='standing_list'),
  path('results/', views.result_list, name='result_list'),
  path('results/<int:pk>', views.result_detail, name='result_detail'),
  path('teams/', views.team_list, name='team_list'),
  path('teams/<int:pk>', views.team_detail, name='team_detail'),
  path('graphs/', views.graphs, name='graphs'),
]

