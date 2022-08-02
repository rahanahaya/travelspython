from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import team
# Create your views here.
def home(request):
    obj=place.objects.all()
    item=team.objects.all()
    return render(request, "index1.html",{'result':obj,'results':item})


# def about (request):
# return render(request,"about.html")
# def contact(request):
# return render(request,"contact.html")
# def detail(request):
# return render(request,"detail.html")
# def thanks (request):
# return  HttpResponse("Thanks")

# def operations(request):
# x=int(request.GET.get('num1'))
# y=int(request.GET.get('num2'))
# add=x+y
# sub=x-y
# mul=x*y
# div=x/y


# return render(request,'result.html',{'addition':add,'subtraction':sub,'multiplication':mul,'division':div})
