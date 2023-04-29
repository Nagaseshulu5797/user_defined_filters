from django.shortcuts import render

# Create your views here.

def filter(request):
    d={'data':'HaI Iam SEhHulu'}
    return render(request,'filter.html',d)