
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    marks1 =90
    marks = 20
    marks = 30
    total = marks1+marks
    return render(request,'index.html',{'total':total})

def gk(request):
    return HttpResponse(request,'index2,html')

def solution(request):
    num1=int(request.POST['number1'])
    num2=int(request.POST['number2'])
    result = num1+num2
    return render(request,'solution.html',{'solution':result})