from django.contrib import admin
from .models import *


# Register your models here.
# admin.site.register(League)
# admin.site.register(Game)

@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    pass

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass
# Define the admin class
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    # list_display = ('name', 'number_game', 'payment')
    pass

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass

