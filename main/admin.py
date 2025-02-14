from django.contrib import admin

from .models import Inventory
admin.site.site_header = "Inventory Manager"
admin.site.site_title = "Inventory Manager Portal"
admin.site.index_title = "Welcome to Inventory Management System"
admin.site.register(Inventory)
# Register your models here.
