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


def account_balance(request):
    
    customer_name = "James"
    account_balance = "19,888"
    next_due_date = "10-10-2016"
    context = {
        
        "title" :"Test View",
        "sum" : sum,
        "customer_name":customer_name,
        "balance":account_balance,
        "next_due_date":next_due_date
    }
    
    return render(request,"test_view.html",context)#view is rendered by test_view.html and context is used to pass variables to test_view.html