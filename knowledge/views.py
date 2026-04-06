from django.shortcuts import render

def knowledge(request):
    return render(request, 'knowledge/home.html')

