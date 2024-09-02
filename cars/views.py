from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    cars = Car.objects.all() 

    return render(
        request, 
        'cars.html',
        {'cars': cars}
    )