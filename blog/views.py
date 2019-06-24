from django.shortcuts import render, redirect, HttpResponse
from django.utils import timezone
from .models import Blog
from .forms import BlogForm

def index(request):
    msg = 'My Message'
    return render(request, 'blog/index.html', {'message':msg})

def list(request):
    blogList = Blog.objects.order_by("-id")
    return render(request, 'blog/list.html', {'blogList': blogList})

def write(request):
    if request.method=="POST":
        dto = Blog(writer=request.POST["writer"],
            title=request.POST["title"],
            content=request.POST["content"])
        dto.save()
        return redirect('/list')

    return render(request, 'blog/write.html')

def detail(request):
    if request.method=="POST":
        bid=request.POST["id"]
        dto=Blog.objects.get(id=bid)
        dto.hit_up()
        dto.save()
        return redirect('/list')
    else:
        bid=request.GET["id"]
        dto=Blog.objects.get(id=bid)
    return render(request, 'blog/detail.html', {"dto":dto})

def edit(request):
    message="Testing"
    b_id=request.POST["id"]
    dto=Blog.objects.get(id=b_id)
    return render(request, 'blog/edit.html', {'dto': dto, 'message':message})

def update(request):
    b_id=request.POST["id"]
    new_dto = Blog(id=b_id,
        writer=request.POST["writer"],
        title=request.POST["title"],
        content=request.POST["content"])
    new_dto.save()
    dto=Blog.objects.get(id=b_id)
    
    return render(request, 'blog/detail.html', {"dto":dto})

def delete(request):
    bid=request.POST["id"]
    dto=Blog.objects.get(id=bid).delete()
    return redirect('/list')

