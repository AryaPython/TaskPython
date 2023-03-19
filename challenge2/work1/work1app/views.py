from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def demo1(request):
    return render(request,'inputing.html')
def addition(request):
       x=int(request.GET['num1'])
       y=int(request.GET['num2'])
       s=x+y
       m=x-y
       t=x*y
       d=x/y
       return render(request,"result.html",{"sum":s,"diff":m,"cross":t,"div":d})

