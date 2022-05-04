from django.contrib import admin
from  .models  import VehicleChecklist, Vehicle, User

admin.site.register(User)
admin.site.register(VehicleChecklist)
admin.site.register(Vehicle)