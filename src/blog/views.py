from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Category, Post
# Create your views here.

@method_decorator(login_required, name='dispatch')
class IndexView(ListView):
    template_name = "blog/index.html"
    queryset = Post.active.all()
    context_object_name = "posts"


@login_required
def post_detail(request, id):
    context = {
        'post': get_object_or_404(Post, pk=id)

    }
    return render(request, 'blog/post_detail.html', context)

