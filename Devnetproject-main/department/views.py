#from django.shortcuts import render
# Create your views here.
from django.shortcuts import render

def department(request):
    return render(request, 'department/home.html')

