from django.shortcuts import render
<<<<<<< HEAD
from django.views.generic import ListView, DetailView
=======
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
>>>>>>> 2f66056f259f9c453f71b2032ac031e77c22dd71
from django.contrib.auth.models import User

@method_decorator(login_required, name='dispatch')
class IndexView(ListView):
    template_name = 'users_list/users_list.html'
    model = User
    context_object_name = "users"
<<<<<<< HEAD


class UserDetailView(DetailView):
    template_name = 'users_list/user_detail.html'
    model = User
    context_object_name = "user"



# Create your views here.
=======
>>>>>>> 2f66056f259f9c453f71b2032ac031e77c22dd71
