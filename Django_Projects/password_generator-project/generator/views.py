from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def home(request):
    #return HttpResponse("hello there friend!")
    #return render(request,'generator/home.html', {"password":"dsfs@656*&^eer"})
    return render(request,'generator/home.html')

def about(request):
    return render(request,'generator/about.html')

def contactus(request):
    return HttpResponse('<h2> This is a contact us page </h2>')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    length = int(request.GET.get('length', 12))

    thepassword =''

    for l in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})
