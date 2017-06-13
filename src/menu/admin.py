from django.contrib import admin
from .models import MainMenu



class MainMenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'position',) #поля, которые надо показывать
    list_editable = ('url', 'position',) #поля для редактирования

admin.site.register(MainMenu, MainMenuAdmin) #какую модель зарегистрировать в админке ,какие модели к ней применить