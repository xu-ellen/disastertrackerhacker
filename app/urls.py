from django.conf.urls import url
from . import views

urlpatterns = [
    url("^$", views.index, name="index"),
    url("^save-earthquake-data/$", views.save_earthquake_data, name="save_earthquake_data"),
]
