from django.shortcuts import render
from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import HttpResponse
from .models import Earthquake
import pandas as pd
import datetime

def index(request):
    return render(request, "app/index.html")


def earthquakes(request):
    return render(request, "app/earthquakes.html", context={
        "earthquakes": list(Earthquake.objects.all())
    })


def forest_fires(request):
    return render(request, "app/forest_fires.html", context={
        "earthquakes": list(Earthquake.objects.all())
    })


def save_earthquake_data(request):
    Earthquake.objects.all().delete() # Clearing table

    data = pd.read_csv(staticfiles_storage.path('hicalix.csv'))
    for index, row in data.iterrows():
        Earthquake.objects.create(
            date=datetime.datetime.strptime(row["Date"], '%m/%d/%Y'),
            latitude=row["Latitude"],
            longitude=row["Longitude"],
            depth=row["Depth"],
            magnitude=row["Magnitude"]
        )

    return HttpResponse("boi")
