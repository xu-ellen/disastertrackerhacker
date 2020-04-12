from django.contrib import admin
from .models import Earthquake, ForestFire, Hurricane

admin.site.register(Earthquake)
admin.site.register(ForestFire)
admin.site.register(Hurricane)
