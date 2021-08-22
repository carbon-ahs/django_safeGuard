from django.shortcuts import render, redirect

def login(request):

    context = {
        'key': 'value',
    }
    return render(request, 'pages/login.html', context)

def index(request):

    context = {
        'key': 'value',
    }
    return render(request, 'pages/index.html', context)