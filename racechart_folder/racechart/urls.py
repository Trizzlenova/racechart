from django.urls import path
from . import views

urlpatterns = [
  # path('', views.see_css, name='see_css'),
  path('getall', views.get_all_races, name='get_all_races'),
  path('drivers/', views.driver_list, name='driver_list'),
  path('drivers/<int:pk>', views.driver_detail, name='driver_detail'),
  path('results/', views.result_detail, name='result_detail'),
]
