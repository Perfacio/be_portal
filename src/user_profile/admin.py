from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile, Department #"." - находится в этом же приложении, импортируем класс Профайл

class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name = 'Профиль'


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInLine, ) #в картеже после посленего элемента всегда запятая


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Department)


# Register your models here.
