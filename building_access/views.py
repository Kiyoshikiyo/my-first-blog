from django.shortcuts import render
from django.http import HttpResponse



def home(request):
#   context = {
#        'posts': .objects.all()
#    }
    return render(request, 'tag/home.html',) #context\n)


def about (request):
    return render(request, 'tag/about.html', {'title': 'About'})
