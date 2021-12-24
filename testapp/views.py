from django.shortcuts import render
from testapp.models import *


# Create your views here.
def index(request):
    return render(request, 'testapphtml/index.html')


def hydjobs(request):
    # jobs_list=Hydjob.objects.all();
    jobs_list = Hydjob.objects.order_by('date')
    my_dict = {'jobs_list': jobs_list}
    return render(request, 'testapphtml/hyderabad.html', context=my_dict)


def bangalorejobs(request):
    return render(request, 'testapphtml/bangalore.html')


def chennaijobs(request):
    return render(request, 'testapphtml/chennai.html')


def punejobs(request):
    return render(request, 'testapphtml/pune.html')
