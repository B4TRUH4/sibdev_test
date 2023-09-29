from django.contrib import admin
from ..models import Gem


@admin.register(Gem)
class GemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
