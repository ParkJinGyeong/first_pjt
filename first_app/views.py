from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return(request, 'index.html')

def root(request):
    return render(request, 'root.html')

def hello(request):

    username = "jin"
    
    context = {
        'username': username
    }

    return render(request, 'hello.html', context)

def lunch(request):
    menus =['김밥', '라면', '돈까스']

    pick = random.choice(menus)

    context = {
        'pick' : pick,
    }
    return render(request, 'lunch.html', context)

def lotto(request):
    
    lotto = str(sorted(random.sample(range(1, 46), 6)))

    context = {
        'lotto' : lotto,
    }
    
    return render(request, 'lotto.html', context)
        