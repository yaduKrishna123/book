from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import bookForm
from .models import book


# Create your views here.
def home(request):
    Book = book.objects.all()
    context = {'booklist': Book}
    return render(request,'home.html',context)

def demo(request):
    Book = book.objects.all()
    context = {'booklist': Book}
    return render(request,'newhome.html',context)
def details(request,book_id):
    Book=book.objects.get(id=book_id)
    return render(request,'newdet.html',{'Book':Book})
def detail(request,book_id):
    Book=book.objects.get(id=book_id)
    return render(request,'detail.html',{'Book':Book})
def add(request):
    if request.method=="POST":
        name=request.POST.get('name')
        dec=request.POST.get('dec')
        year=request.POST.get('year')
        img=request.FILES['img']
        Book=book(name=name,dec=dec,year=year,img=img)
        Book.save()
    return render(request,'add.html')
def update(request,id):
    Book=book.objects.get(id=id)
    form=bookForm(request.POST or None,request.FILES,instance=Book)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'Book':Book})
def delete(request,id):
    if request.method=='POST':
        Book=book.objects.get(id=id)
        Book.delete()
        return redirect('/')
    return render(request,'delete.html')


