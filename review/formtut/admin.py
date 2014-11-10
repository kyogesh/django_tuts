from django.contrib import admin
from .models import Person

class PersonAdmin(admin.ModelAdmin):

    list_display = ['name', 'birth_date', 'image']
    fieldsets = [
        (None , {'fields':['name']}),
        ('Birth Info', {'fields':['birth_date', 'birth_place']}),\
        ('Image', {'fields': ['image']}),
    ]
    search_fields = ['name']

admin.site.register(Person, PersonAdmin)