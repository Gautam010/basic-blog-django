from django.shortcuts import render,redirect
from .models import *
from .forms import *
def index(request):
    records=Post.objects.all().order_by('-id')[1:]
    last_post=Post.objects.all().order_by('-id')[0]
    return render(request,'index.html',{'rec':records,'last':last_post})

def create_post(request):
    if request.method=='POST':
        form=Post_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form=Post_form()
        records=Post.objects.all()

    return render(request,'post.html',{'form':form})