from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
#    return HttpResponse('hello nora')
    return render(request,'home.html')

def product_view(request):
    return render(request,'product.html')
