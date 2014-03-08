from django.contrib import admin
from arescaler.models import *

class ItemAdmin(admin.ModelAdmin):
    list_display  = ["name", "size"]

admin.site.register(Item, ItemAdmin)
