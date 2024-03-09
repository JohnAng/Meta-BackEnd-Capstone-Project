from django.contrib import admin
from .models import Booking, Menu

DBs = [Booking, Menu]
# Register your models here.
admin.site.register(DBs)
