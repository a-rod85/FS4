from django.contrib import admin

# Register your models here.

from .models import Restaurant, Table, Reservations, Menu


admin.site.register(Restaurant)
admin.site.register(Table)
admin.site.register(Reservations)
admin.site.register(Menu)

