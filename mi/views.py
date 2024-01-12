from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def miteam1(request):
    return render(request,'mi.html')

def miteam2(request):
    return HttpResponse('This is the page of miteam2')


