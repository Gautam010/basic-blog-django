from django.shortcuts import render,redirect
from .models import *
from .forms import *
def index(request):
    records=Post.objects.all().order_by('-id')[1:]
    last_post=Post.objects.all().order_by('-id')[0]
    return render(request,'index.html',{'rec':records,'last':last_post})

def create_post(request):
    if request.method=='POST':
        form=Post_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form=Post_form()

    return render(request,'post.html',{'form':form})

def detail(request,x):
    r=Post.objects.get(id=x)
    return render(request,'detail.html',{'s':r})

def delete(request,x):
    r = Post.objects.get(id=x)
    r.delete()
    return redirect("index")
