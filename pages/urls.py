from django.urls import path 
from . import views 

urlpatterns = [
    path('cars/' , views.viewCars , name ="viewCars"),
     path('task1/' , views.task1 , name ="viewtask1"),

]
