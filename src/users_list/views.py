from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@method_decorator(login_required, name='dispatch')
class IndexView(ListView):
    template_name = 'users_list/users_list.html'
    model = User
    context_object_name = "users"


@method_decorator(login_required, name='dispatch')
class UserDetailView(DetailView):
    template_name = 'users_list/user_detail.html'
    model = User
    context_object_name = "user"
    image = "image"
