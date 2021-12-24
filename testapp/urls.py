from django.urls import path
from testapp import views

urlpatterns = [
    path('index/', views.index),
    path('hyd/', views.hydjobs),
    path('bangalore/', views.bangalorejobs),
    path('chennai/', views.chennaijobs),
    path('pune/', views.punejobs),
]
