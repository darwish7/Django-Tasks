from django.shortcuts import render
from django.http import HttpResponse
from .models import Car 

# Create your views here.

def viewCars(request):
       return render(request,'pages/cars.html', {"cars":Car.objects.all().order_by('model').exclude(name="lancer")})
 
def task1(request):
    newdic =[{"user":"ziad","age":22,"salary":100000},{"user":"gasser","age":26,"salary":60000},{"user":"mostafa","age":27,"salary":70000}]
    dic = {"users" : newdic}
    return render(request,'pages/task1.html',dic)