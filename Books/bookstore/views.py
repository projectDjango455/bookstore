from django.shortcuts import render

# Create your views here.
def funcHome(request):
    return render(request,'bookstore/index.html')