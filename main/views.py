from django.shortcuts import render

# Create your views here.

def noteMate(request):
    return render(request,'index.html')