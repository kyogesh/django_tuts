from django.contrib import admin
from .models import Person

class PersonAdmin(admin.ModelAdmin):

    list_display = ['name', 'birth_date']
    fieldsets = [
        (None , {'fields':['name']}),
        ('Birth Info', {'fields':['birth_date', 'birth_place']}),
    ]
    search_fields = ['name']

admin.site.register(Person, PersonAdmin)