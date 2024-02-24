from django.shortcuts import render,redirect
from .models import *

def cars(request):
    brands = Brand.objects.all()
    cars = Models.objects.all()
    context = {
        'brands':brands,
        'cars': cars
    }
    return render(request, 'home.html', context)

def car(request, car_id):
    return render(request, 'car.html', {'car': Models.objects.get(id=car_id)})

def create(request):
    if request.method == 'POST':
        brand = Brand.objects.get(id=request.POST.get('brand'))
        model = request.POST.get('model')
        price = request.POST.get('price')
        cover = request.FILES.get('cover')
        volume = request.POST.get('volume')
        status = request.POST.get('status')
        Models.objects.create(brand=brand,model=model,price=price,cover=cover,volume=volume,status=status)
        return redirect('home')
    return render(request,'create.html', {'brands': Brand.objects.all(), 'statuses': Models.Status.choices})

def detail(requsest, course_id):
    course = Models.objects.get(id = course_id)
    return render(requsest,'detail.html',{'course': course})

def update(requsest, course_id):
    car = Models.objects.get(id = course_id)
    if requsest.method == 'POST': 
        car.model = requsest.POST.get('model')
        car.brand = requsest.POST.get('brand')
        car.volume = requsest.POST.get('volume')
        car.price = requsest.POST.get('price')
        car.status = requsest.POST.get('status')
        car.cover = requsest.FILES.get('cover')
        car.save()
        return redirect('detail',course_id)
    return render(requsest,'update.html',{'car': car})

def delete(request, course_id):
    car = Models.objects.get(id = course_id)
    car.delete()
    return redirect('list')
