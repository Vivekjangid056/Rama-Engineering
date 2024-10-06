from django.contrib import admin
from .models import Projects, Products, Clients, Team, Services, Banner, AboutUs

# Register your models here.

admin.site.register(Projects)
admin.site.register(Products)
admin.site.register(Clients)
admin.site.register(Team)
admin.site.register(Services)
admin.site.register(Banner)
admin.site.register(AboutUs)
