from django.contrib import admin
from .models import Employee, Position, Item ,Department, Antivirus

admin.site.register(Employee)
admin.site.register(Position)
admin.site.register(Item)
admin.site.register(Department)
admin.site.register(Antivirus)