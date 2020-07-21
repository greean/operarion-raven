from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cities", views.cities, name="cities"),
    path("<int:event_id>/", views.event, name="event"),
    path("cities/<str:city_name>/", views.city, name="city"),

]