from django.shortcuts import redirect,render,get_object_or_404
from .models import Data
from django.http import HttpResponse
from django.utils import timezone
import json
import datetime
from .forms import DateForm
# Create your views here.

def grab(request):
    pollution = request.GET['pol']
    latitude = request.GET['lat']
    longitude = request.GET['lon']

    Data.objects.create(pollution=pollution,latitude=latitude,longitude=longitude)

    return redirect("showMap")

def showMap(request):
    # date = datetime.date.today()
    # if request.GET['date']:
    #     date = request.GET['date']

    form = DateForm()
    return render(request,"pms/Dashboard_mist/pages/maps.html",{'f':form})