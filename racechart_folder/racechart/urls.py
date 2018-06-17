from django.urls import path
from . import views

urlpatterns = [
  # path('', views.see_css, name='see_css'),
  path('getall', views.get_all, name='get_all'),
  # path('create_driver', views.create_driver, name='create_driver'),
  path('drivers/', views.driver_list, name='driver_list'),
  path('drivers/<int:pk>', views.driver_detail, name='driver_detail'),
]
