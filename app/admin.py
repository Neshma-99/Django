from django.contrib import admin
from app.models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['fullname','emp_code','mobile','position','address']
admin.site.register(Employee,EmployeeAdmin)