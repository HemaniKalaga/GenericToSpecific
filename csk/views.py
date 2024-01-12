from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def msd1(request):
    return render(request,'csk.html')

def msd2(request):
    return HttpResponse('This is a page of csk msd2')

