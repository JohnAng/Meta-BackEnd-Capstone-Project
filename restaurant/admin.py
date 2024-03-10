from django.contrib import admin
from .models import Booking, MenuItem

DBs = [Booking, MenuItem]
# Register your models here.
admin.site.register(DBs)
