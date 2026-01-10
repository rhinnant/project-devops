from django.shortcuts import render

# Create your views here.
def assets(request):
    return render (request, 'assets/home.html')
