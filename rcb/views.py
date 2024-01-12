from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def virat1(request):
    return render(request,'rcb.html')

def virat2(request):
    return HttpResponse('This is rcb virat2 view page of HttpResponse')
