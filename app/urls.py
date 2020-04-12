from django.conf.urls import url
from . import views

urlpatterns = [
    url("^$", views.index, name="index"),
    url("^earthquakes/$", views.earthquakes, name="earthquakes"),
    url("^forest-fires/$", views.forest_fires, name="forest_fires"),
    url("^hurricanes/$", views.hurricanes, name="hurricanes"),

    url("^save-earthquake-data/$", views.save_earthquake_data, name="save_earthquake_data"),
    url("^save-forestfire-data/$", views.save_forestfire_data, name="save_forestfire_data"),
    url("^save-hurricane-data/$", views.save_hurricane_data, name="save_hurricane_data"),

    url("^api/predict-earthquake-stats/$", views.predict_earthquake_stats, name="predict_earthquake_stats"),
]
