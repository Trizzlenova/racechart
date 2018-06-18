from django.urls import path, include
from django.conf.urls import url
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
  path('', views.standing_list, name="standing_list"),
  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
  url(r'api/races/$', views.RaceList.as_view()),
  path('api/races/<int:pk>', views.race_detail, name="race_detail"),
  url(r'api/standings/$', views.StandingList.as_view()),
  url(r'api/standings/(?P<pk>[0-9]+)/$', views.StandingList.as_view()),
  url(r'api/results/$', views.ResultList.as_view()),
  url(r'api/results/(?P<pk>[0-9]+)/$', views.ResultDetail.as_view()),
  path('getall', views.get_all_races, name='get_all_races'),
  path('drivers/', views.driver_list, name='driver_list'),
  path('drivers/<int:pk>', views.driver_detail, name='driver_detail'),
  path('standings/', views.standing_list, name='standing_list'),
  path('graphs/', views.graphs, name='graphs'),
  # path('results/', views.result_detail, name='result_detail'),
]
