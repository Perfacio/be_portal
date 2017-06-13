from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import User


class IndexView(ListView):
    template_name = 'users_list/users_list.html'
    model = User
    context_object_name = "users"






# Create your views here.
