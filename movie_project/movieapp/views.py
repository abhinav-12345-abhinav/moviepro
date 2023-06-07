from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import movieform
from .models import movie
# Create your views here.
def index(request):
    abc=movie.objects.all()
    context={
        'movies':abc
    }
    return render(request,'index.html',context)
def details(request,movie_id):
    abcd=movie.objects.get(id=movie_id)
    return render(request,"details.html",{'abc':abcd})

def add(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc=request.POST.get('desc',)
        year=request.POST.get('year',)
        img=request.FILES['img']
        movies=movie(name=name,desc=desc,year=year,img=img)
        movies.save()
    return render(request,'add.html')

def update(request,id):
    Movie=movie.objects.get(id=id)
    form=movieform(request.POST or None,request.FILES,instance=Movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movies':Movie})

def delete(request,id):
    if request.method=='POST':
        Movie=movie.objects.get(id=id)
        Movie.delete()
        return redirect('/')
    return render(request,'delete.html')

