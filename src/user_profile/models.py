from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=300, verbose_name='Отдел')


    def __str__(self):
        return self.name


class Profile(models.Model): #создать новую таблицу в бд
    user = models.OneToOneField(User, on_delete=models.CASCADE) #cвязь пользлвателя и профиля, взаимосвязь при удалении
    patronymic = models.CharField(max_length=150, verbose_name='Отчество')
    department = models.ForeignKey(Department, related_name='users')
    birthday = models.DateField(blank=True) #blanck - необязательное для заполнения
    mobile_phone = models.CharField(max_length=12, verbose_name='Телефон')
    work_phone = models.CharField(max_length=10, verbose_name='Внутренний телефон', blank=True)
    #TODO: добавить фотографию профиля

# Create your models here.
