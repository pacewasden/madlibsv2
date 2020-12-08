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
