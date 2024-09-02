# cars/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Car, VehicleLocation, DropOff
from django.views.decorators.csrf import csrf_exempt
import json

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {'cars': cars})

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'car_detail.html', {'car': car})

def car_create(request):
    if request.method == "POST":
        make = request.POST.get('make')
        model = request.POST.get('model')
        year = int(request.POST.get('year'))
        mileage = int(request.POST.get('mileage'))
        color = request.POST.get('color')
        Car.objects.create(make=make, model=model, year=year, mileage=mileage, color=color)
        return redirect('car_list')
    return render(request, 'car_form.html')

def car_update(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == "POST":
        car.make = request.POST.get('make')
        car.model = request.POST.get('model')
        car.year = int(request.POST.get('year'))
        car.mileage = int(request.POST.get('mileage'))
        car.color = request.POST.get('color')
        car.save()
        return redirect('car_list')
    return render(request, 'car_form.html', {'car': car})

def car_delete(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == "POST":
        car.delete()
        return redirect('car_list')
    return render(request, 'car_confirm_delete.html', {'car': car})

@csrf_exempt
def receive_gps_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        car_id = data.get('car_id')
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        car = Car.objects.get(id=car_id)
        VehicleLocation.objects.create(car=car, latitude=latitude, longitude=longitude)

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

def drop_off(request, car_id, location_id):
    car = get_object_or_404(Car, id=car_id)
    location = get_object_or_404(VehicleLocation, id=location_id)
    DropOff.objects.create(car=car, location=location)
    return redirect('drop_off_list')

def drop_off_list(request):
    drop_offs = DropOff.objects.all()
    return render(request, 'drop_off_list.html', {'drop_offs': drop_offs})
