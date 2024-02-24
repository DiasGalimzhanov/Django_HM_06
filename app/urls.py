from django.urls import path
from .views import *

urlpatterns = [
    path('', cars, name='home'),
    path('create/', create, name='create'),
    path('car/<int:car_id>/', car, name='car'),

]