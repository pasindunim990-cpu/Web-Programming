from django.contrib import admin
from .models import Player, Position

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("name", "specialist")
    list_filter = ("specialist",)
    search_fields = ("name",)

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "team", "age")
    list_filter = ("team", "positions")
    search_fields = ("first_name", "last_name", "team")
    filter_horizontal = ("positions", "approved_specialist_positions")
