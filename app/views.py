from django.shortcuts import render
from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import HttpResponse
from .models import Earthquake
import pandas as pd
import datetime

def index(request):
    return render(request, "app/index.html", context={
        "earthquakes": Earthquake.objects.all()
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
