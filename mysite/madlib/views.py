from django.shortcuts import render,redirect
from .forms import WordForm
from .models import Words

# Create your views here.

def index(request):
     return render(request, 'madlib/index.html')


def word_list(request):
    form = WordForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/gameview1.html')
    return render(request, 'madlib/game1.html', {'form':form})

def gameview(request):
    word_list = Words.objects.filter()[:1].get()
    context = {
        'word_list': word_list,
    }
    return render(request, 'madlib/gameview1.html', context)


def deletewords(request):
    word_list = Words.objects.filter()[:1].get()
    if request.method == 'POST':
        word_list.delete()
        return redirect('madlib:index')
    return render(request, 'madlib/deleteword.html',{'word_list':word_list})

#This is view 2
def word_list2(request):
    form = WordForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/gameview2.html')
    return render(request, 'madlib/game2.html', {'form':form})

def gameview2(request):
    word_list = Words.objects.filter()[:1].get()
    context = {
        'word_list': word_list,
    }
    return render(request, 'madlib/gameview2.html', context)

#This is view 3
def word_list3(request):
    form = WordForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/gameview3.html')
    return render(request, 'madlib/game3.html', {'form':form})

def gameview3(request):
    word_list = Words.objects.filter()[:1].get()
    context = {
        'word_list': word_list,
    }
    return render(request, 'madlib/gameview3.html', context)
#This is view 4
def word_list4(request):
    form = WordForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/gameview4.html')
    return render(request, 'madlib/game4.html', {'form':form})

def gameview4(request):
    word_list = Words.objects.filter()[:1].get()
    context = {
        'word_list': word_list,
    }
    return render(request, 'madlib/gameview4.html', context)
#This is view 5
def word_list5(request):
    form = WordForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/gameview5.html')
    return render(request, 'madlib/game5.html', {'form':form})

def gameview5(request):
    word_list = Words.objects.filter()[:1].get()
    context = {
        'word_list': word_list,
    }
    return render(request, 'madlib/gameview5.html', context)
