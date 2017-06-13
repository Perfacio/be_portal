from django.db import models
from django.urls import NoReverseMatch
from django.urls import reverse


class MainMenu(models.Model):
    name = models.CharField(max_length=256, verbose_name="Наименование")
    url = models.CharField(max_length=256, verbose_name="Django-URL", help_text="blog:index")
    position = models.IntegerField(default=1000)

    def get_url(self):
        try:
            return reverse(self.url)
        except NoReverseMatch:
            return ""

    class Meta:
        ordering = ['position', 'name']
        verbose_name = 'Пункты меню'
        verbose_name_plural = 'Пункт меню'

    def __str__(self):
        return self.name
