from django.shortcuts import render
from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import HttpResponse
from .models import Earthquake, ForestFire, Hurricane
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
        "forest_fires": list(ForestFire.objects.all())
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


def save_forestfire_data(request):
    ForestFire.objects.all().delete() # Clearing table

    data = pd.read_csv(staticfiles_storage.path('Fires.csv'))
    for index, row in data.iterrows():
        ForestFire.objects.create(
            name=row["FIRE_NAME"],
            year=row["FIRE_YEAR"],
            latitude=row["LATITUDE"],
            longitude=row["LONGITUDE"],
        )

    return HttpResponse("boi")


def save_hurricane_data(request):
    Hurricane.objects.all().delete() # Clearing table

    data = pd.read_csv(staticfiles_storage.path('full.csv'))
    for index, row in data.iterrows():
        Hurricane.objects.create(
            # date=row["Date"],
            name="Hurricane",
            latitude=float(row["Latitude"][:-1]),
            longitude=float(row["Longitude"][:-1]),
        )

    return HttpResponse("boi")
