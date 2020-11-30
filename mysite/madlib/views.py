from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'madlib/index.html')

def game1(request):
    return render(request, 'madlib/game1.html')

def game2(request):
    return render(request, 'madlib/game2.html')

def game3(request):
    return render(request, 'madlib/game3.html')

def game4(request):
    return render(request, 'madlib/game4.html')

def game5(request):
    return render(request, 'madlib/game5.html')