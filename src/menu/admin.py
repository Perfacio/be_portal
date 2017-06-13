from django.contrib import admin
from .models import MainMenu



class MainMenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'position',)
    list_editable = ('url', 'position',)

admin.site.register(MainMenu, MainMenuAdmin)