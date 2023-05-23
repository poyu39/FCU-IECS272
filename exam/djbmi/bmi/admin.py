from django.contrib import admin
from .models import People

# Register your models here.
class PeopleAdmin(admin.ModelAdmin):
    list_display = ("pname", "tall", "weight")

admin.site.register(People, PeopleAdmin)