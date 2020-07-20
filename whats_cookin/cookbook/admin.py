from django.contrib import admin

# Register your models here.

from .models import Recipe

admin.site.register(Recipe)
admin.site.site_header = "What's Cookin' (Admin)"
