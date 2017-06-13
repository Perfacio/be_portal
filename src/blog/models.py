from django.db import models
from django.contrib.auth.models import User


class IsActiveManager(models.Manager):

    def get_queryset(self):
        return super(IsActiveManager, self).get_queryset().filter(is_active=True)

class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название категории', unique=True)
    is_active = models.BooleanField(default=True)
    objects = models.Manager()
    active = IsActiveManager()

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    author = models.ForeignKey(User, verbose_name='Пользователь')
    category = models.ForeignKey(Category, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    objects = models.Manager()
    active = IsActiveManager()


    class Meta:
        ordering = ["-created_at"] #cортировка по дате создания в обратном порядке "-"

    def __str__(self):
        # return "{title} | {desc}".format(title=self.title, desc=self.description[:20])   #функция строкового представляния Python
        return self.title

