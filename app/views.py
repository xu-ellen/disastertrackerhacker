from django.shortcuts import render
from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import HttpResponse, JsonResponse
from .models import Earthquake, ForestFire, Hurricane
import numpy as np
import pandas as pd
import pickle
import boto3
from sklearn.ensemble import RandomForestRegressor
import datetime
import time

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

def hurricanes(request):
    return render(request, "app/hurricanes.html", context={
        "hurricanes": list(Hurricane.objects.all())
    })


def save_earthquake_data(request):
    Earthquake.objects.all().delete() # Clearing table

    data = pd.read_csv(staticfiles_storage.path('database.csv'))
    for index, row in data.iterrows():
        try:
            Earthquake.objects.create(
                date=datetime.datetime.strptime(row["Date"], '%m/%d/%Y'),
                latitude=row["Latitude"],
                longitude=row["Longitude"],
                depth=row["Depth"],
                magnitude=row["Magnitude"]
            )
        except:
            pass

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


# API PREDICTION ROUTES
def predict_earthquake_stats(request):
    lat = request.GET.get("lat")
    lng = request.GET.get("lng")

    dt = datetime.datetime(2020, 4, 12, 0, 0, 0)
    if request.GET.get("date"):
        date = request.GET.get("date")
        date_list = [int(i) for i in date.split("-")]
        dt = datetime.datetime(date_list[0], date_list[1], date_list[2], 0, 0, 0)

    date = time.mktime(dt.timetuple())

    cred = boto3.Session().get_credentials()
    ACCESS_KEY = cred.access_key
    SECRET_KEY = cred.secret_key

    s3client = boto3.client('s3',
                            aws_access_key_id = ACCESS_KEY,
                            aws_secret_access_key = SECRET_KEY,
                           )

    response = s3client.get_object(Bucket='calix-assets', Key='finalized_model.sav')
    print(response)
    body = response['Body'].read()
    print(body)
    loaded_model = pickle.loads(body)

    user_input = [lat, lng, date]  # takes user input
    user_array = np.asarray(user_input).reshape(1,-1)

    # loaded_model = pickle.load(open(filename, 'rb'))
    predict = loaded_model.predict(user_array)

    return JsonResponse({
        "magnitude": predict[0][0],
        "depth": predict[0][1],
        "lat": lat,
        "lng": lng
    })
