from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User


class IndexView(ListView):
    template_name = 'users_list/users_list.html'
    model = User
    context_object_name = "users"


class UserDetailView(DetailView):
    template_name = 'users_list/user_detail.html'
    model = User
    context_object_name = "user"



# Create your views here.
