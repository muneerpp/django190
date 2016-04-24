from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.

def posts_create(request):
    context = {

        "title": "create"

    }
    return render(request, "index.html", context)


def posts_details(request, id=None):
    instance = get_object_or_404(Post, id=id)

    context = {

        "title": "Details",
        "instance": instance

    }
    return render(request, "post_detail.html", context)


def posts_list(request):
    queryset = Post.objects.all()
    if request.user.is_authenticated():
        context = {
            "title": "Admin"
        }
    else:
        context = {
            "object_list": queryset,
            "title": "List"

        }
    return render(request, "index.html", context)


def posts_update(request):
    context = {

        "title": "Update"

    }
    return render(request, "index.html", context)


def posts_delete(request):
    context = {

        "title": "Delete"

    }
    return render(request, "index.html", context)
