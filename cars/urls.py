# cars/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('car/<int:pk>/', views.car_detail, name='car_detail'),
    path('car/new/', views.car_create, name='car_create'),
    path('car/<int:pk>/edit/', views.car_update, name='car_update'),
    path('car/<int:pk>/delete/', views.car_delete, name='car_delete'),
    path('gps/', views.receive_gps_data, name='receive_gps_data'),
    path('dropoff/<int:car_id>/<int:location_id>/', views.drop_off, name='drop_off'),
    path('dropoffs/', views.drop_off_list, name='drop_off_list'),
]
