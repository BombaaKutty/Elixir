from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def gallery(request):
    return render(request,'gallery.html')

def information(request):
    return render(request,'info.html')

def table2(request):
    return render(request,'assinfo.html')

def regi(request):
    return render(request,'registration.html')

def login(request):
    return render(request,'login.html')