from django.shortcuts import render, get_object_or_404
from .models import Category, Post
# Create your views here.


def index_page(request):
    context = {
        'categories': Category.active.all(), #запрос к бд, получаем все активные категории
    }
    if request.GET.get("q"):
        cat_id = request.GET.get("q") #GET - словарь, get - взятие словаря
        context["posts"] = Post.objects.filter(category_id=cat_id)
    else:
        context["posts"] = Post.active.all()

    return render(request, 'blog/index.html', context)


def post_detail(request, id):
    context = {
        'post': get_object_or_404(Post, pk=id)

    }
    return render(request, 'blog/post_detail.html', context)

