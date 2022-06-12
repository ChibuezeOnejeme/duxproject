from django.contrib import admin

# Register your models here.
from.models import Searched_data,Chart_table

class DataAdmin(admin.ModelAdmin):
    list_display = ('label','data','user')# gives table view in admin for chart_table

admin.site.register(Searched_data)
admin.site.register(Chart_table,DataAdmin)