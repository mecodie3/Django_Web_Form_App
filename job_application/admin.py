from django.contrib import admin
from .models import Form

#Class to customize what we want to see in Admin Interface
class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","email")
     #to add search bar widget
    search_fields = ("first_name", "last_name", "email")
    list_filter =("date","occupation")
    ordering=("first_name",) #("-first_name",)-> minus for reverse order
    #specify which field to read
    readonly_fields=("occupation",)

admin.site.register(Form,FormAdmin)

